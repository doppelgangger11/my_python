from abc import ABC, abstractmethod


class Film(ABC):
    def __init__(self, title, released, director, box_office, duration, rating):
        self.title = title
        self.released = released
        self.director = director
        self.box_office = box_office
        self.duration = duration
        self.rating = rating
    
    def get_name(self):
        print(self.title)
    
    def change_name(self):
        self.title = input("Please enter a new title of film >>> ")
        print("New title of film is", self.title)
    
    def get_director(self):
        print(self.director)
    
    @abstractmethod

    def show_info(self):
        print("---------------------")
        print("The title is >>>", self.title)
        print("Dirctor >>>", self.director)
        print("---------------------")
        print("Relised in >>>", self.released)
        print("The box office in USD >>>", self.box_office)
        print("Duratin in minutes >>>", self.duration)
        print("Reating in rotten tomatos >>>", self.rating)
        print("---------------------")

class Anime(Film):
    def __init__(self, title, released, director, box_office, duration, rating, manga, opening_title, ending_title):
        super().__init__(title, released, director, box_office, duration, rating)
        self.manga = manga
        self.opening = opening_title
        self.ending = ending_title
    def get_manga(self):
        print("Name of manga >>>", self.manga)
    def show_info(self):
        super().show_info()
        print("Name of mnga >>>", self.manga)
        print("Opening title is >>>", self.opening)
        print("Ending title is >>>", self.ending)
        print("---------------------")