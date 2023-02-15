from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import sqrt
from typing import List


class Vector4(ABC):
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    def __add__(self, v):
        new_x = self.x + v.x
        new_y = self.y + v.y
        new_z = self.z + v.z
        new_w = self.w + v.w
        new_obj = Vector4(new_x, new_y, new_z, new_w)
        return new_obj
    def __mul__(self, v):
        new_x = self.x * v.x
        new_y = self.y * v.y
        new_z = self.z * v.z
        new_w = self.w * v.w
        return f"multy = {new_x + new_y + new_z + new_w}"
    def __str__(self):
        return f"beautiful output >>> {self.x}, {self.y}, {self.z}, {self.w}"
    def __eq__(self, v):
        if self.x == v.x and self.y == v.y and self.z == v.z and self.w == v.w:
            return True
        else:
            return False
    def __le__(self, v):
        my_laight = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)
        leight_2 = sqrt(v.x ** 2 + v.y ** 2 + v.z ** 2 + v.w ** 2)
        if my_laight <= leight_2:
            return True
        else:
            return False
    def __it__(self, v):
        my_laight = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)
        leight_2 = sqrt(v.x ** 2 + v.y ** 2 + v.z ** 2 + v.w ** 2)
        if my_laight < leight_2:
            return True
        else:
            return False
        
@dataclass
class Film:
    name: str
    director: str
    year: int
    cash: float
    
    def set_name(self, new_name):
        last_name = self.name
        self.name = new_name
        return f"Film's has changed from '{last_name}' to '{self.name}'"
    def get_director(self):
        return f"Name of Director {self.director}"
    def get_cash(self):
        return self.cash
    

if __name__ == "__main__":
    v1 = Vector4(1, 2, 3, 4)
    v2 = Vector4(1, 2, 3, 4)
    print(v1)
    print(v2)
    print(v1 + v2)
    print(v1.__mul__(v2))
    print(v1.__eq__(v2))
    print(v1.__le__(v2))

    film1 = Film("asd", "dsa", 1, 1.2)
    film2 = Film("sad", "asdasd", 1, 1.9)
    print(film1.set_name("sdasd"))
    print(film1.get_director())
    print(film1.get_cash())
    print(film1 + film2)