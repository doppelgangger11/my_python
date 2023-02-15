class Shop:
    def __init__(self, list_price, basket):
        self.l = dict(list_price)
        self.basket = basket
    
    # function for adding    
    def add(self, products):
        for i in products:
            if i == self.keys_l:
                self.basket.append(i)
        return self.basket
    
    # function for removing
    def rem(self, product):
        for i in range(len(self.basket)):
            if product(i) in self.basket():
                self.basket.remove(product(i))
        return self.basket
    
    # function fo printing your basket
    def get_basket(self, bs):
        cur_bs = []
        for i in bs:
            if i not in cur_bs:
                cur_bs.append(i)
        print(cur_bs)

    # getting sum
    def get_sum_prices(self, bas, s):
        for i in self.l.keys():
            for j in range(len(bas)):
                if i in bas[j]:
                    s = s + self.l[i]
        print(s)
    
    # function for inputing
    def imp(self):
        command = input('enter your comand :')
        return command

price_list = {'chicken' : 1900, 'energy_drink' : 450, 'cigarettes' : 720}
bas = []
cur_bas = []
s = 0

run = True

while run:
    
    n = Shop(price_list, bas)

    com = n.imp()

    pr_add = None
    pr_rem = None
    
    if com == 'add' or com == 'add ':
        print(price_list, ' ', 'enter your products:')
        pr_add = input().split()
        cur_bas = n.add(pr_add)
        # for i in pr_add:
        #     cur_bas.append(i)
        print(cur_bas, ': that is your basket!')
        # com = None
        # com = n.imp()
    
    if com == 'remove' or com == 'remove ':
        print(cur_bas, ' ', 'What do you want to remove?')
        pr_rem = input().split()
        n.rem(pr_rem)
        for i in pr_rem:
            cur_bas.remove(i)
        print(cur_bas, ' ', ': that is your basket!')
        # com = None
        # com = n.imp()
    
    if com == 'price' or com == 'price ':
        n.get_sum_prices(cur_bas, s)
        s = 0
        # com = None
        # com = n.imp()

    if com == 'basket' or com == 'basket ':
        n.get_basket(cur_bas)
        # com = None
        # com = n.imp()

    if com == 'help' or com == 'help ':
        print('Current commands: add, remove, price, basket, (q or exit), help')
        print('to enter a command, you need type it without "spaces"')

    if com == 'price_list' or com == 'price_list ':
        print(price_list)
    
    if com == 'q' or com == 'exit' or com == 'q ' or com == 'exit ':
        run = False