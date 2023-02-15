class Bibibka:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def summ(self):
        return self.a + self.b
    
    def minus(self):
        return self.a - self.b
    
    def multi(self):
        return self.a * self.b
    
    def devi(self):
        return self.a / self.b

run = True
run2 = True
while run == True:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: ")) 
    d = Bibibka(a, b)

    while run2 == True:
        comand = input("Lets use comads: ")
        if comand.strip() == "q": # .strip() - убирает пробелы " "
            run = False
            run2 = False
        elif comand == "+":
            print(d.summ())
        elif comand == "-":
            print(d.minus())
        elif comand == "*":
            print(d.multi())
        elif comand == "/":
            print(d.devi())
        else:
            print("please enter commands: '+', '-', '*', '/' or 'q'")