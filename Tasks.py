from typing import List

from colorama import Back, Fore, Style, init

# @dataclass
# class Task:
    # name: str
    # description: str
    # date: List
    # deadline: List
    # priority: bool

    # I was try, but ;(

init()


class Task:
    def __init__(self, name: str, description: str, date: List, deadline: List, priority: bool=False):
        type = Task
        self.name = name
        self.description = description
        self.date = date
        self.deadline = deadline
        self.priority = priority

        if self.priority == True:
            self.priority_str = "It's very important!!!"
        else:
            self.priority_str = "It's not very important"
    
    # try to create a priority for self.date but it isn't working 
    
    def __str__(self):
        return Fore.RED + f'''
---------------
{self.name}
---------------
{self.description}
---------------
date of record: {self.date[0]}.{self.date[1]}.{self.date[2]}
deadline: {self.deadline[0]}.{self.deadline[1]}.{self.deadline[2]}
---------------
{self.priority_str}
---------------''' + Style.RESET_ALL

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

class TaskManager:
    def __init__(self, file_adress: str):
        self.loc = file_adress
        self.tasks = []

    def __str__(self):
        return f'''{[print(i) for i in self.tasks]}'''

    def add_task(self, task):
        self.tasks.append(task)
        
    def write_txt(self):
        with open(self.loc, "w") as t:
            for i in self.tasks:
                t.write(f'''name: {i.name}
description: {i.description}
date of record: {i.date[0]}.{i.date[1]}.{i.date[2]}
deadline: {i.deadline[0]}.{i.deadline[1]}.{i.deadline[2]}
priority: {i.priority_str}
#
''')

    def closing_task(self, name: str):
        for i in self.tasks:
            if i.name == name:
                self.tasks.remove(i)
        self.write_txt()

    def changing_task(self, name_of_task: str, type_of: str, new_value=None):
        for i in self.tasks:
            if i.name == name_of_task:
                if type_of == "name":
                    i.name = new_value
                elif type_of == "description":
                    i.description = new_value
                elif type_of == "deadline":
                    if new_value == "":
                        i.deadline = [None, None, None]
                    else:
                        i.deadline = new_value
                elif type_of == "priority":
                    if i.priority == True:
                        i.priority = False
                    else:
                        i.priority = True
                    print("---------------")
                    print(f"Priority has changed to: {i.priority}")
                    print("---------------")

    def notyfication(self, today_date):
        c1 = 0
        c2 = 0
        print(Fore.RED + f"Tomorrow's tasks: ")
        for i in self.tasks:
            c1 += 1
            if today_date[2] == i.deadline[2]:
                if today_date[1] == i.deadline[1]:
                    if today_date[0] + 1 == i.deadline[0]:
                        print(i)
                        c2 += 1
        if c1 != c2:
            print("There is no tasks for tomorrow")
        print(Style.RESET_ALL)

    def reading_txt(self):
        with open(self.loc, "r") as file:
            text = file.read()
            text = text.split("#")
            final_text_list = []
            for i in text:
                i = str(i)
                i = i.split("\n")
                final_text_list.append(i)
            self.tasks = []
            for i in range(len(final_text_list) - 1):
                if i != 0:
                    final_text_list[i].remove('')
                    final_text_list[i].remove('')
                elif i == 0:
                    final_text_list[i].remove('')

                name = final_text_list[i][0].replace("name: ", "")
                description = final_text_list[i][1].replace("description: ", "")
                date = final_text_list[i][2].replace("date of record: ", "").split(".")
                deadline = final_text_list[i][3].replace("deadline: ", "").split(".")
                deadline = [int(i) for i in deadline]
                priority = final_text_list[i][4].replace("priority: ", "")                    

                if priority == "It's very important!!!":
                    priority = True
                elif priority == "it's not very important":
                    priority = False

                self.add_task(Task(name, description, date, deadline, priority))
            final_text_list.pop(-1)

    def todays_tasks(self, today_date):
        for i in self.tasks:
            if today_date == i.deadline:
                print("This is the tasks for today: ")
                print(i)

    def only(self, sett):
        for i in self.tasks:
            buffer_str = None
            if i.priority == "It's very important!!!":
                buffer_str = "True"
            elif i.priority == "It's not very important": 
                buffer_str = "False"
            if buffer_str == sett:
                print(i)
                
    def clear_tasks(self):
        self.tasks = []
    