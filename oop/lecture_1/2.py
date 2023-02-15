class Phone:
    def __init__(self, name, phone, weight):
        self.mane = name
        self.phone = phone
        self.weight = weight
    def recevie_call(self, name):
        print(name, "is call you")
    def get_number(self):
        print(self.phone)
    def all_info(self):
        print(self.mane, self.phone, self.weight)

a = Phone("samsung", "87073738825", 12)

a.recevie_call("Misha")
a.get_number()
a.all_info()