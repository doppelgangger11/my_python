from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    
    @property
    def age(self):
        return self.__age 
    
    @age.setter
    def age(self, new_age):
        self.__age = new_age

if __name__ == "__main__":
    p1 = Person("asd", 12, 213123)
    p2 = Person("asdasd", 38, 949947)
    p1.age += p2.age
    print(p1.age)