from abc import ABC


class Vehicle(ABC):
    def __init__(self, owner, max_speed, weight, number_of_weels, petrol_type):
        self.owner = owner
        self.m_speed = max_speed
        self.weight = weight
        self.n_weels = number_of_weels
        self.petrol_type = petrol_type
    def go_straight(self):
        print("Now you are accelireating")
    def go_back(self):
        print("You pushing the break")
        print("Then, you change gear to reverse")
        print("and go back")
    def turn_left(self):
        print("Turn the steering weel to left, and turn left")
    def turn_right(self):
        print("Turn the steering weel to right, and turn right")

class Car(Vehicle):
    def __init__(self, owner, max_speed, weight, number_of_weels, petrol_type, numbe_of_motor_cylinders):
        super().__init__(owner, max_speed, weight, number_of_weels, petrol_type)
        self.n_cylinders = numbe_of_motor_cylinders
        self.fog_lights = False
    def turn_fog_lights(self):
        if self.fog_lights == False:
            self.fog_lights = True
            print("Fog lights is now on!")
        else:
            self.fog_lights = False
            print("Fog lights is now off!")
    def fast_stop(self):
        print("You turn the emergency lights and fast breaking")

        
class Motorcycle(Vehicle):
    def __init__(self, owner, max_speed, weight, number_of_weels, petrol_type, motor_hourse_power):
        super().__init__(owner, max_speed, weight, number_of_weels, petrol_type)
        self.motor_hp = motor_hourse_power
    def turn_left_lights(self):
        print("You turn on the left lights")
        self.turn_left()
    def turn_right(self):
        print(print("You turn on the right lights"))
        self.turn_right()
        
class Bicycle(Vehicle):
    def __init__(self, owner, max_speed, weight, number_of_weels, petrol_type, have_bell):
        super().__init__(owner, max_speed, weight, number_of_weels, petrol_type)
        self.bell = have_bell
    def bring_bell(self):
        print("Bring")
    def stop(self):
        print("You pushing to the trigger of breaker and stopping")