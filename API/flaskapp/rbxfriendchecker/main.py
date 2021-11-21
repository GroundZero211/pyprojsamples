from flask import Flask, render_template, make_response, abort
from requests import get, post
import secrets, os, random

app = Flask(__name__, template_folder='templates')

@app.route('/users/<int:userid>/friendlist')
def index(userid):
    response = get(os.getenv('URL1').format(userid))
    response2 = get(os.getenv('URL2').format(userid))
    if response.status_code == 503: abort(503)
    json_data2= response2.json()
    json_data = response.json()
    key = list(json_data.keys())
    if key[0] == 'data' and json_data[key[0]] == []:
        return "Empty Friends"
    elif key[0] == 'errors':
        return "{} {}".format(json_data[key[0]][0]['message'], json_data[key[0]][0]['userFacingMessage'])
    friendListPresence = [
		'Offline' if json_data['data'][i]['presenceType'] == 0 \
		else 'Online' if json_data['data'][i]['presenceType'] == 1 \
		else 'Ingame' if json_data['data'][i]['presenceType'] == 2 \
		else 'Studio' for i in range(len(json_data['data']))
	]
    fake_tokens = [secrets.token_hex() for i in range(len(json_data['data']))]
    r = make_response(render_template('base.html', userid=userid,random_int=random.randint(30, 60), mf=json_data, fr=friendListPresence, r=len(json_data['data']), token=fake_tokens, json_data2=json_data2))
    r.headers.set('X-Content-Type-Options', 'nosniff')
    r.headers.set('X-Frame-Options', 'SAMEORIGIN')
    r.headers.set('X-XSS-Protection', '1; mode=block')
    return r

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/users/<int:userid>/profile')
def profile(userid):
    response = post(os.getenv('URL3'), data={"userIds": [userid]})
    response2 = get(os.getenv('URL4').format(userid))
    json_data = response.json()
    json_data2 = response2.json()
    gen_fakehash = secrets.token_hex(32) if json_data['userPresences'][0]['userPresenceType'] == 2 else None # if user is ingame then generate random hash.. :D
    r = make_response(render_template('userinf.html',fakehash=gen_fakehash, json_data=json_data, json_data2=json_data2))
    r.headers.set('X-Content-Type-Options', 'nosniff')
    r.headers.set('X-Frame-Options', 'SAMEORIGIN')
    r.headers.set('X-XSS-Protection', '1; mode=block')
    return r

app.run(host='0.0.0.0', port=8080, debug=True)
