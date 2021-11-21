class Car:
    def __init__(self, max_speed, speed_unit):
        self.max_speed = max_speed
        self.speed_unit = speed_unit

    def __str__(self):
        return 'Car with the maximum speed of %s %s' % (self.max_speed, self.speed_unit) 

class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return 'Boat with the maximum of %s knots' % self.max_speed

if __name__ == '__main__':
    # number of queries
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
            print(vehicle)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
            print(vehicle)
        else:
            raise ValueError("invalid vehicle type")
