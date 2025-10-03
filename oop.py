class Student :
    def __init__(self,name,surname,age,student_id ,course):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__student_id = student_id
        self.__course =course
    def get_full_name(self):
        return f"ismi : {self.__name} familyasi : {self.__surname}"
    def get_age(self):
        return f"age : {self.__age}"
    def get_student_id(self):
        return f"ID : {self.__student_id}"
    def get_course(self):
        return f"course : {self.__course}"
    def set_age(self,new_age):
        self.__age = new_age
    def set_student_full_name(self,name,surname):
        self.__name = name
        self.__surname = surname
    def increase_course(self):
        if self.__course < 4:
            self.__course+=1
    def update_student_id(self,new_id):
        self.__student_id = new_id
s1 = Student("Rahmatulla","Yuldshbayev",18,"ID1008",3)
print(s1.get_full_name())
print(s1.get_age())
print(s1.get_student_id())
print(s1.get_course())
s1.set_age(19)
print(s1.get_age())
s1.set_student_full_name("Abbos","Tusunboyev")
print(s1.get_full_name())
s1.increase_course()
print(s1.get_course())
s1.update_student_id("ID1009")
print(s1.get_student_id())
