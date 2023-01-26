class Student:
    def __init__(self, name, surename, student_id, gender, course, faculty, speciality, number):
        self.full_name = name + ' ' + surename
        self.id = student_id
        self.s_course = course
        self.s_faculty = faculty
        self.speciality = speciality
        self.subjects = []
        self.semester = 1
        self.number = number
        self.gender = gender
    def all_info(self):
        print("----------------------")
        print("Order of Student is:", self.number)
        print("Full name and ID:")
        print(self.full_name, self.id)
        print("Gender >>>", self.gender)
        print("----------------------")
        print("Course >>> ", self.s_course)
        print("Faculty >>> ", self.s_faculty)
        print("Speciality >>> ", self.speciality)
        print("Semestr >>> ", self.semester)
        print("----------------------")
        print("Subjects: ")
        for i in range(len(self.subjects)):
            print(self.subjects[i])
        print("----------------------")
    def get_full_name(self):
        if self.gender == "F" or self.gender == "f":
            print("Her name is >>> ", self.full_name)
        elif self.gender == "M" or self.gender == "m":
            print("His name is >>> ", self.full_name)
    def add_subject(self, sub):
        for i in sub:
            self.subjects.append(i)
    def semester_change(self):
        self.semester += 1
        self.subjects = []

class Faculty:
    def __init__(self, name, dean):
        self.faculty_name = name
        self.dean = dean
        self.students = []
    def add_students(self, student): # students <- "stud1.full_name"
        self.students.append(student)
    def show_students(self):
        print("Here is all student in this faculty >>> ")
        for i in self.students: # i -> class Student
            print(i.all_info())
            print("------------------------")


stud1 = 1
stud2 = 1
stud3 = 1
stud4 = 1
stud5 = 1
stud6 = 1
fac1 = 1
fac2 = 1
fac3 = 1

run = True

print("----------------------")
print("you can create 6 Student and 3 faculty")
print("----------------------")

while run == True:
    
    list_stud1 = []
    list_stud2 = []

    comand = input("Please enter your command >>> ").strip()

    if comand == "q":
        run = False
    elif comand == "help":
        print("main comands:", "q, help")
        print("comands for students:", "add_student, full_name, all_info, semestr_change, add_subjects")
        print("comands for faculty:", "create_faculty, add_student_to_faculty, show_students")
    elif comand == "add_student":
        if stud1 == 1:
            stud1 = Student(input("Plaese, enter the name of Student >>> ").strip(), input("Plaese, enter the surename of Student >>> ").strip(), input("Plaese, enter ID of Student >>> ").strip(), input("Please, enter gender of Student (F, f or M, m) >>> ").strip(), input("Plaese, enter course of Student >>> ").strip(), input("Plaese, enter faculty of Student >>> ").strip(), input("Plaese, enter speciality of Student >>> ").strip(), 1)
        elif stud1 != 1 and stud2 == 1:
            stud2 = Student(input("Plaese, enter the name of Student >>> ").strip(), input("Plaese, enter the surename of Student >>> ").strip(), input("Plaese, enter ID of Student >>> ").strip(), input("Please, enter gender of Student (F, f or M, m) >>> ").strip(), input("Plaese, enter course of Student >>> ").strip(), input("Plaese, enter faculty of Student >>> ").strip(), input("Plaese, enter speciality of Student >>> ").strip(), 2)
        elif stud1 != 1 and stud2 != 1 and stud3 == 1:
            stud3 = Student(input("Plaese, enter the name of Student >>> ").strip(), input("Plaese, enter the surename of Student >>> ").strip(), input("Plaese, enter ID of Student >>> ").strip(), input("Please, enter gender of Student (F, f or M, m) >>> ").strip(), input("Plaese, enter course of Student >>> ").strip(), input("Plaese, enter faculty of Student >>> ").strip(), input("Plaese, enter speciality of Student >>> ").strip(), 3)
        elif stud1 != 1 and stud2 != 1 and stud3 != 1 and stud4 == 1:
            stud4 = Student(input("Plaese, enter the name of Student >>> ").strip(), input("Plaese, enter the surename of Student >>> ").strip(), input("Plaese, enter ID of Student >>> ").strip(), input("Please, enter gender of Student (F, f or M, m) >>> ").strip(), input("Plaese, enter course of Student >>> ").strip(), input("Plaese, enter faculty of Student >>> ").strip(), input("Plaese, enter speciality of Student >>> ").strip(), 4)
        elif stud1 != 1 and stud2 != 1 and stud3 != 1 and stud4 != 1 and stud5 == 1:
            stud5 = Student(input("Plaese, enter the name of Student >>> ").strip(), input("Plaese, enter the surename of Student >>> ").strip(), input("Plaese, enter ID of Student >>> ").strip(), input("Please, enter gender of Student (F, f or M, m) >>> ").strip(), input("Plaese, enter course of Student >>> ").strip(), input("Plaese, enter faculty of Student >>> ").strip(), input("Plaese, enter speciality of Student >>> ").strip(), 5)
        elif stud1 != 1 and stud2 != 1 and stud3 != 1 and stud4 != 1 and stud5 != 1 and stud6 == 1:
            stud6 = Student(input("Plaese, enter the name of Student >>> ").strip(), input("Plaese, enter the surename of Student >>> ").strip(), input("Plaese, enter ID of Student >>> ").strip(), input("Please, enter gender of Student (F, f or M, m) >>> ").strip(), input("Plaese, enter course of Student >>> ").strip(), input("Plaese, enter faculty of Student >>> ").strip(), input("Plaese, enter speciality of Student >>> ").strip(), 6)
    elif comand == "all_info":
        comand2 = input("Please enter the full name of student >>> ").strip()
        if comand2 == stud1.full_name:
            stud1.all_info()
        elif comand2 == stud2.full_name:
            stud2.all_info()
        elif comand2 == stud3.full_name:
            stud3.all_info()
        elif comand2 == stud4.full_name:
            stud4.all_info()
        elif comand2 == stud5.full_name:
            stud5.all_info()
        elif comand2 == stud6.full_name:
            stud6.all_info()
        else:
            print("Please repeat a comand")
    elif comand == "full_name":
        comand2 = input("Please enter the number of Student, if there is in base >>> ").strip()
        if comand2 == "1":
            stud1.get_full_name()
        elif comand2 == "2":
            stud2.get_full_name()
        elif comand2 == "3":
            stud3.get_full_name()
        elif comand2 == "4":
            stud4.get_full_name()
        elif comand2 == "5":
            stud5.get_full_name()
        elif comand2 == "6":
            stud6.get_full_name()
        else:
            print("Please repeat a comand")
    elif comand == "semestr_change":
        comand2 = input("Please enter the full name of Student >>> ").strip()
        if comand2 == stud1.full_name:
            stud1.semester_change()
        elif comand2 == stud2.full_name:
            stud2.semester_change()
        elif comand2 == stud3.full_name:
            stud3.semester_change()
        elif comand2 == stud4.full_name:
            stud4.semester_change()
        elif comand2 == stud5.full_name:
            stud5.semester_change()
        elif comand2 == stud6.full_name:
            stud6.semester_change()
        else:
            print("Please repeat a comand")
    elif comand == "add_subjects":
        comand2 = input("Please enter the full name of Student >>> ").strip()
        if comand2 == stud1.full_name:
            l = input("Please enter subjects of Student >>> ").split()
            stud1.add_subject(l)
        elif comand2 == stud2.full_name:
            l = input("Please enter subjects of Student >>> ").split()
            stud2.add_subject(l)
        elif comand2 == stud3.full_name:
            l = input("Please enter subjects of Student >>> ").split()
            stud3.add_subject(l)
        elif comand2 == stud4.full_name:
            l = input("Please enter subjects of Student >>> ").split()
            stud4.add_subject(l)
        elif comand2 == stud5.full_name:
            l = input("Please enter subjects of Student >>> ").split()
            stud5.add_subject(l)
        elif comand2 == stud6.full_name:
            l = input("Please enter subjects of Student >>> ").split()
            stud6.add_subject(l)
        else:
            print("Please repeat full name")
    elif comand == "create_faculty":
        if fac1 == 1:
            print("This is first faculty in base")
            fac1 = Faculty(input("Please enter the name of Faculty >>> "), input("Please enter the Dean of Faculty >>> "))
        elif fac1 != 1 and fac2 == 1:
            print("This is second faculty in base")
            fac2 = Faculty(input("Please enter the name of Faculty >>> "), input("Please enter the Dean of Faculty >>> "))
        elif fac1 != 1 and fac2 != 1 and fac3 == 1:
            print("This is third faculty in base")
            fac3 = Faculty(input("Please enter the name of Faculty >>> "), input("Please enter the Dean of Faculty >>> "))
    elif comand == "add_student_to_faculty":
        comand2 = input("Please enter the name of Faculty >>> ")
        if fac1 != 1:
            if comand2 == fac1.faculty_name:
                comand3 = input("Please enter the names of Students >>> ").split()
                for i in range(len(comand3) - 1): 
                    list_stud1.append(comand3[i] + ' ' + comand3[i + 1])
                for k in range(len(list_stud1)):
                    if k % 2 == 0:
                        list_stud2.append(list_stud1[k])
                for j in list_stud2:
                    if j == stud1.full_name:
                        fac1.add_students(stud1)
                    elif j == stud2.full_name:
                        fac1.add_students(stud2)
                    elif j == stud3.full_name:
                        fac1.add_students(stud3)
                    elif j == stud4.full_name:
                        fac1.add_students(stud4)
                    elif j == stud5.full_name:
                        fac1.add_students(stud5)
                    elif j == stud6.full_name:
                        fac1.add_students(stud6)
                    else:
                        print(j, "not in base")
        if fac2 != 1:
            if comand2 == fac2.faculty_name:
                comand3 = input("Please enter the names of Students >>> ").split()
                for i in range(len(comand3) - 1): 
                    list_stud1.append(comand3[i] + ' ' + comand3[i + 1])
                for k in range(len(list_stud1)):
                    if k % 2 == 0:
                        list_stud2.append(list_stud1[k])
                for j in list_stud2:
                    if j == stud1.full_name:
                        fac2.add_students(stud1)
                    elif j == stud2.full_name:
                        fac2.add_students(stud2)
                    elif j == stud3.full_name:
                        fac2.add_students(stud3)
                    elif j == stud4.full_name:
                        fac1.add_students(stud4)
                    elif j == stud5.full_name:
                        fac1.add_students(stud5)
                    elif j == stud6.full_name:
                        fac1.add_students(stud6)
                    else:
                        print(j, "not in base")
        if fac3 != 1:
            if comand2 == fac3.faculty_name and fac3 != 1:
                comand3 = input("Please enter the names of Students >>> ").split()
                for i in range(len(comand3) - 1): 
                    list_stud1.append(comand3[i] + ' ' + comand3[i + 1])
                for k in range(len(list_stud1)):
                    if k % 2 == 0:
                        list_stud2.append(list_stud1[k])
                for j in list_stud2:
                    if j == stud1.full_name:
                        fac3.add_students(stud1)
                    elif j == stud2.full_name:
                        fac3.add_students(stud2)
                    elif j == stud3.full_name:
                        fac3.add_students(stud3)
                    elif j == stud4.full_name:
                        fac1.add_students(stud4)
                    elif j == stud5.full_name:
                        fac1.add_students(stud5)
                    elif j == stud6.full_name:
                        fac1.add_students(stud6)
                    else:
                        print(j, "not in base")
    elif comand == "show_students":
        comand2 = input("Please, enter the name of Faculty >>> ").strip()
        if comand2 == fac1.faculty_name:
            fac1.show_students()
        elif comand2 == fac2.faculty_name:
            fac2.show_students()
        elif comand3 == fac3.faculty_name:
            fac3.show_students()
        else:
            print("There is no Faculty with this name, please try again")
    else:
        print("There is no comand like this, please enter 'help' to see all comands")
