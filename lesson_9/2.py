from time import sleep


class WheelsType:
    SPORT = 1
    REGULAR = 2


class BodyType:
    SEDAN = 1
    LONG = 2


class Car:
    def __init__(self, engine, max_speed, wheels_type, body_type, acceleration):
        self.engine = engine
        self.max_speed = max_speed
        self.wheels_type = wheels_type
        self.body_type = body_type
        self.acceleration = acceleration

    def __calculate_wheels(self):
        if self.wheels_type == WheelsType.SPORT:
            self.acceleration *= 1.1
        else:
            self.acceleration *= 0.9

    def __calculate_body_type(self):
        if self.body_type == BodyType.SEDAN:
            self.acceleration *= 1.2
        else:
            self.acceleration *= 0.9

    def __go_to_max(self):
        current_speed = 0.0
        while current_speed < self.max_speed:
            print(f"Current speed: {current_speed}")
            current_speed += self.acceleration
            sleep(1)
        return current_speed - self.acceleration

    def go_to_max(self):
        self.__calculate_wheels()
        self.__calculate_body_type()
        last_speed = self.__go_to_max()
        print("Finish 🏁")
        print(f"Last speed: {last_speed} 🏁")


bmw = Car(3.0, 300.0, WheelsType.SPORT, BodyType.SEDAN, 50)
vw = Car(1.6, 240.0, WheelsType.REGULAR, BodyType.LONG, 40)

bmw.go_to_max()
vw.go_to_max()