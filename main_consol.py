import datetime

from colorama import Back, Fore, Style, init
from Tasks import Task, TaskManager

if __name__ == "__main__":
    
    # init of programm

    init()

    task_mangr = TaskManager("./tasks.txt")
    today = str(datetime.date.today())
    today = today.split("-")
    today = today[::-1]
    today = [int(i) for i in today]
    
    update_mode = None

    try:
        with open("./settings.txt", "x") as f:
            update_mode = input(Fore.CYAN + "Please enter the mode 'autosave' or 'manualsave' >>> ").strip()
            f.write(update_mode)
            print("All settings are saved" + Style.RESET_ALL)
    except FileExistsError:
        pass

    print(Fore.RED + "<<<If you want to change the settings, enter the command 'main settings>>>'" + Style.RESET_ALL)

    with open("./settings.txt") as f:
        for line in f:
            if line == "autosave" or line == "manualsave":
                update_mode = line
            else:
                print(Fore.RED + "<<<Settings is not correct, please change the settings>>>" + Style.RESET_ALL)
    
    # autosave
    # manualsave

    # if you don't have tasks.txt this shit will create it

    try:
        with open("./tasks.txt", "x") as f:
            pass
    except FileExistsError:
        pass


    
    if update_mode == "autosave":
        print(Fore.CYAN + "<<< All changes saved automatically >>>" + Style.RESET_ALL)

    print(Fore.CYAN + "<<< Initializing complete >>>" + Style.RESET_ALL)

    # notify about tomorrow's tasks

    task_mangr.reading_txt()
    task_mangr.notyfication(today)

    run = True
    while run:
        
        print(Fore.GREEN + "Please enter your command" + Style.RESET_ALL)
        com = input(Fore.BLUE + ">>> " + Style.RESET_ALL).strip()
        
        for i in task_mangr.tasks:
            i.name == ""
            task_mangr.closing_task("")
        
        if update_mode == "autosave":
            task_mangr.reading_txt()
        
        if com == "help":
            if update_mode == "autosave":
                print(Fore.CYAN + "There is the main commands: help, q" + Style.RESET_ALL)
                print(Fore.CYAN + "There is tasks commands: show tasks, add new task, tomorrow's tasks, close the task, change the task, today's tasks, show tasks with priority, clear tasks" + Style.RESET_ALL)
            elif update_mode == "manualsave":
                print(Fore.CYAN + "There is the main commands: help, q" + Style.RESET_ALL)
                print(Fore.CYAN + "There is tasks commands: show tasks, add new task, tomorrow's tasks, close the task, change the task, today's tasks, show tasks with priority, clear tasks" + Style.RESET_ALL)
                print(Fore.YELLOW + "Addition commands: read, write" + Style.RESET_ALL)
        
        elif com == "change settings":
            run2 = True
            while run2:
                pre_update_mode = input(Fore.GREEN + "Please enter a new updating mode 'autosave' or 'manualsave' >>> " + Style.RESET_ALL).strip()
                if pre_update_mode == "autosave" or pre_update_mode == "manualsave":
                    with open("./settings.txt", "w") as f:
                        f.write(pre_update_mode)
                    update_mode = pre_update_mode
                    print(Fore.CYAN + "<<< Complete >>>" + Style.RESET_ALL)
                    run2 = False
                else:
                    print(Fore.RED + "Please try again" + Style.RESET_ALL)

        elif com == "q":
            if update_mode == "autosave":
                task_mangr.write_txt()
            run = False
            print(Fore.MAGENTA + "Thanks for using this programm <3" + Style.RESET_ALL)

        elif com == "clear tasks":
            com2 = input(Fore.RED + "Are you sure [y, n]? >>> " + Style.RESET_ALL).strip()
            task_mangr.clear_tasks()
        
        elif com == "tomorrow's tasks":
            task_mangr.notyfication(today)

        elif com == "show tasks":
           print(task_mangr)
        
        elif com == "add new task":
            name = input(Fore.YELLOW + "Please enter the name >>> " + Style.RESET_ALL).strip()
            discription = input(Fore.YELLOW + "Please enter your description >>> " + Style.RESET_ALL).strip()
            deadline = input(Fore.YELLOW + f"Please enter the date of deadline like '{today[0]} {today[1]} {today[2]}' >>> " + Style.RESET_ALL).split()
            priority = bool(input(Fore.YELLOW + "Please enter the piority 'True' if it's very important (if not, just press 'Enter' button) >>> " + Style.RESET_ALL).strip())

            if deadline == []:
                deadline = [0, 0, 0]
                
            task_mangr.add_task(Task(name, discription, today, deadline, priority))
            print(Fore.CYAN + "<<< Complete >>>" + Style.RESET_ALL)
        
        elif com == "close the task":
            print(task_mangr)
            task_mangr.closing_task(input(Fore.RED + "Please enter the name of task for close it >>> " + Style.RESET_ALL).strip())
            print(Fore.CYAN + "<<< Complete >>>" + Style.RESET_ALL)
        
        elif com == "change the task":
            print(task_mangr)
            name = input(Fore.YELLOW + "Please enter the name of task that you want to change >>> " + Style.RESET_ALL).strip()
            creteria = input(Fore.YELLOW + "Please enter the creteria that you want to change >>> " + Style.RESET_ALL).strip() 
            if creteria == "priority":
                task_mangr.changing_task(name, creteria)
                print(Fore.CYAN + "<<< Complete >>>" + Style.RESET_ALL)
            else:
                new_value = input(Fore.YELLOW + "Please enter a new value of creteria >>> " + Style.RESET_ALL).strip()
                task_mangr.changing_task(name, creteria, new_value)
                print(Fore.CYAN + "<<< Complete >>>" + Style.RESET_ALL)
        
        elif com == "today's tasks":
            task_mangr.todays_tasks(today)
        
        elif com == "show tasks with priority":
            task_mangr.only(input(Fore.YELLOW + "Please enter the piority 'True' for important of 'False' for not important >>> " + Style.RESET_ALL))
        
        elif com == "read":
            if update_mode == "manualsave":
                task_mangr.reading_txt()
                print(Fore.CYAN + "<<< Complete >>>" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"There is no comand like {com}, please try again" + Style.RESET_ALL)
        elif com == "write":
            if update_mode == "manualsave":
                task_mangr.write_txt()
                print(Fore.CYAN + "<<< Complete >>>" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"There is no comand like {com}, please try again" + Style.RESET_ALL)   
        
        
        else:
            print(Fore.RED + f"There is no comand like {com}, please try again" + Style.RESET_ALL)
        
        if update_mode == "autosave":
            task_mangr.write_txt()