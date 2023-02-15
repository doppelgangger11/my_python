class Car:
    def __init__(self, mark, color, years, dtp):
        self.car_mark = mark
        self.color = color
        self.years = years
        self.dtp = dtp
    
    def get_attrs(self):
        print(self.car_mark)
        print(self.color)
        print(self.years)
        print(self.dtp)

    def dtp_false_rule(self):
        if self.years < 2000 and self.dtp == False:
            print("maybe it's not right")



car_1 = Car('bmw', 'black', 1991, False)

car_1.get_attrs()
car_1.dtp_false_rule()