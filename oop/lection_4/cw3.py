from dataclasses import dataclass


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

@dataclass
class Student:
    mane: str
    id: int
    grade = {}

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, subject, grade):
        self.__grade.get[subject] = grade
    
    
if __name__ == "__main__":
    std1 = Student("asd", 2039)

    std1.grade('assddds', "asdsdsda")
    print(std1.grade) 