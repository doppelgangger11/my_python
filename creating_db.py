import sqlite3

class Data_dase:
    def __init__(self, name):
        self.name = name

    def comand(self):
        com = input('what do you want to input: ')
        return com
    
    def inputing_data(self):
        inp = input()
        return inp

    def inputing_heads(self, c):
        a = c.execute('''CREATE TABLE articles ({self.inputing_data()})''')
        return a
    
    def inputing_values(self, c):
        a = c.execute("INSERT INTO articles VALUES ( " + self.inputing_data() + " )")
        return a

a = input('Type name of DB: ')

run = True
while run:

    db = Data_dase(a)
    db_1 = sqlite3.connect(db.name + '.db')
    c = db_1.cursor()
    com = db.comand()

    if com == 'input heads' or com == 'input heads ':
        db.inputing_heads(c)
        db_1.commit()
    elif com == 'input values' or com == 'input values ':
        db.inputing_values(c)
        db_1.commit()
    elif com == 'q' or com == 'q ':
        run = False
    else:
        print('current comands: input heads, input values')