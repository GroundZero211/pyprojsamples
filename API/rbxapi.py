import requests, os
import pandas as pd

class RbxAPI:
    def __init__(self, cookie_value):
        self.cookie_name = '.ROLOSECURITY'
        self.cookie_value = cookie_value

    def get_rbxrequest(self, method, url, **kwargs):
        session = requests.Session()
        session.cookies.set(self.cookie_name, self.cookie_value)
        request = session.request(method, url, **kwargs)
        if method == "POST" or method == "PUT" or method == "PATCH" or method == "DELETE":
            if "x-csrf-token" in request.headers:
                session.headers["x-csrf-token"] = request.headers["x-csrf-token"]
                if request.status_code == 403:
                    request = session.request(method, url, **kwargs)
        return request

class Presence:
    def __init__(self, cookie_value, userid):
        self.cookie_name = '.ROBLOSECURITY'
        self.cookie_value = cookie_value
        self.userid = userid

    def get_presence(self):
        friendlistreq = requests.get(os.getenv('url1').format(self.userid))
        json_data = friendlistreq.json()
        listuserids = [json_data['data'][i]['id'] for i in range(len(json_data['data']))]
        
        req = RbxAPI.get_rbxrequest(self, "POST", os.getenv('url2'), data={"userIds": listuserids})
        
        json_data2 = req.json()
                
        df = pd.DataFrame(
            {
                "UserID":   [json_data2['userPresences'][i]['userId'] for i in range(len(json_data2['userPresences']))],
                "Username": [json_data['data'][i]['name'] for i in range(len(json_data2['userPresences']))],
                "OnlineStatus": ["Offline" if json_data2['userPresences'][i]['userPresenceType'] == 0 else "Online/Website" if json_data2['userPresences'][i]['userPresenceType'] == 1 else "Ingame" if json_data2['userPresences'][i]['userPresenceType'] == 2 else "Studio" for i in range(len(json_data2['userPresences']))],
                "serverID": [json_data2['userPresences'][i]['gameId'] for i in range(len(json_data2['userPresences']))],
                "lastLocation":  [json_data2['userPresences'][i]['lastLocation'] if json_data2['userPresences'][i]['lastLocation'] == "Website" else "Authorization not allowed" if json_data2['userPresences'][i]['lastLocation'] == "" else json_data2['userPresences'][i]['lastLocation'] for i in range(len(json_data2['userPresences']))],
                "lastActive":   [json_data2['userPresences'][i]['lastOnline'] for i in range(len(json_data2['userPresences']))]
            }
        )
        return df
    
    def __str__(self):
        pd.set_option("display.max_rows", None)
        return str(Presence.get_presence(self))

if __name__ == '__main__':
    userid = input("Enter your userid: ")
    rbxcookie = input("rbx cookie: ")
    rbxapi = Presence(rbxcookie, userid)
    print(rbxapi)
