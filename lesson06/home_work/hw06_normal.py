# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__ (self, surname, name,  fathername, father, mother):
        self.surname = surname
        self.name = name
        self.fathername = fathername
        self.father = father
        self.mother = mother
 
    
    def parents(self):  #Узнать родителей указанного ученика
        print("Отец - ", self.father, ", мать - ", self.mother)
    
    def get_full_name (self):
        return self.name + ' ' + self.surname
    
class Stud(Person):
    def __init__ ( self , surname, name , fathername,  father, mother, cla = "1a"):
        super().__init__ ( surname, name, fathername, father, mother)
        self.cla = cla 
    def cl ( self ):
        return self.cla 
                               
class Teacher ( ):
    def __init__ ( self , name ,  cl_s , subj):
#        Person . __init__ ( self , name)
        self . name = name
        self . cl_s = cl_s
        self . subj = subj


stud_1 = Stud( "Иванов" , "Ваня" , "Петрович" , "Петр Васильевич Иванов", "Марья Романовна Иванова" , "5а")
stud_2 = Stud( "Петров" , "Миша" , "Иванович" , "Иван Иванович Петров", "Татьяна Васильевна Петрова" , "5а")
stud_3 = Stud( "Сидоров" , "Петя" , "Евгеньевич" , "Евгений Иванович Сидоров", "Настасья Сидоров" , "1б")
stud_4 = Stud( "Степин" , "Вася" , "Захарович" , "Захар Егорович Степин", "Матрена Никифоровна Степина" , "5а")

teach_1 = Teacher("Дудкин Борис Иванович","5а", "Математика")
teach_2 = Teacher("Жиглов Николай Васильевич","5а", "Чтение")
teach_3 = Teacher("Соколова Татьяна Михайловна", "1б", "Пение")

students = [stud_1, stud_2, stud_3, stud_4]
teachers = [teach_1, teach_2, teach_3]

# 1. Получить полный список всех классов школы
def all_class():
    all_class = []
    for i in students:
        all_class.append(i.cla)
    uniq_class = set(all_class)
    return uniq_class

# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
def stud_in_cla():
    in_cl = input("Введите класс ")
    stud_list = []
    for i in students:
        if i.cla == in_cl:
            a = i.surname + " " +i.name[0] + "." + i.name[0] + "."
            stud_list.append(a)                             
    return stud_list

# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)




def subj_list(a):
    subjects = []
    for i in teachers:
        if i.cl_s == a:
            subjects.append(i.subj)
    return subjects


# 4. Вернуть id ученика по фамилии
def stud_surname(surname):
    for i in students:
        if i.surname == surname:
            return i
        
#5. Получить список всех Учителей, преподающих в указанном классе

def teach_in_cla(cla):
    teach_in_class = []
    for i in teachers:
        if i.cl_s == cla:
            teach_in_class.append(i.name)
    return teach_in_class

ans=True
while ans:
    print("""
 1. Получить полный список всех классов школы
 2. Получить список всех учеников в указанном классе
  (каждый ученик отображается в формате "Фамилия И.О.")
 3. Получить список всех предметов указанного ученика 
  (Ученик --> Класс --> Учителя --> Предметы)
 4. Узнать ФИО родителей указанного ученика
 5. Получить список всех Учителей, преподающих в указанном классе
 6. Выход
    """)
    ans=input("Что необходимо сделать? ")
    if ans=="1":
        print(*all_class())
    elif ans=="2":
        print("Список учеников: ", *stud_in_cla())
    elif ans=="3":
        print("3. Получить список всех предметов указанного ученика ")
        x = stud_surname(input("Введите фамилию "))
        print(*subj_list(x.cla))
    elif ans=="4":
        print("Узнать родителей указанного ученика")
        # a = input("Введите фамилию ")
        Person.parents(stud_surname(input("Введите фамилию ")))
    elif ans=="5":
        print("5. Получить список всех Учителей, преподающих в указанном классе") 
        print(', '.join(map(str, teach_in_cla(input("Введите класс ")))) )
    elif ans=="6":
        print("\n Goodbye")   
        ans = None
    else:
        print("\n Not Valid Choice Try again")