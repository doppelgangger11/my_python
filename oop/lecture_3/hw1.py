
# >>> I don't understand what is this pice of **** (5.  <, <=, >, >= — сравниваете число элементов)

class MyList:
    def __init__(self, elements):
        self.elements = list(elements)
    
    def __add__(self, l):
        el = []
        for i in self.elements:
            el.append(int(i))
        r = True
        new_l = []
        while r == True:
            if len(el) > len(l.elements):
                l.elements.append(0)
            elif len(el) < len(l.elements):
                el.append(0)
            else:
                for i in range(len(el)):
                    d = el[i] + l.elements[i]
                    new_l.append(d)
                r = False
        # self.elements = new_l
        return new_l
    
    def __sub__(self, l):
        el = []
        for i in self.elements:
            el.append(int(i))
        r = True
        new_l = []
        while r == True:
            if len(el) > len(l.elements):
                l.elements.append(0)
            elif len(el) < len(l.elements):
                el.append(0)
            else:
                for i in range(len(el)):
                    el[i] -= l.elements[i]
                    new_l.append(el[i])
                r = False
        # self.elements = new_l
        return new_l
    
    def __len__(self):
        return len(self.elements)
    
    def ____(self, l):
        pass

    
    def __str__(self):
        l = self.elements
        l_str = str()
        for i in range(len(l)):
            l[i] = str(l[i])
            l_str += l[i] + " "
        return l_str

    def append(self, n):
        self.elements.append(n)
    
    def pop(self):
        self.elements.pop()

    def max(self):
        if len(self.elements) > 0:
            return max(self.elements)
        else:
            return "there is no elements"

    def min(self):
        if len(self.elements) > 0:
            return min(self.elements)
        else:
            return "there is no elements"


a = MyList(int(i) for i in input("Enter the first list of numbers >>> ").split())
b = MyList(int(i) for i in input("Enter the second list of numbers >>> ").split())
print(a)
a.append(3)
print(a)
a.pop()
print(a)
print(a.max())
print(a.min())
print(a - b)
print(a + b)