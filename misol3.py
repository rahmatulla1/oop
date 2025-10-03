from abc import ABC ,abstractmethod

class Employee(ABC):
    def __init__(self,name,salary:float = 0):
        self.name = name
        self.salary = salary
        super().__init__()

    @abstractmethod
    def get_details(self):
        pass
    @abstractmethod
    def calculate_bonus(self):
        pass
class Manager(Employee):
    def __init__(self, name, department ,salary = 0):
        self.department = department
        super().__init__(name, salary)
    def get_details(self):
        print( f"name:{self.name} Department :{self.department} salary:{self.salary} ")
    def calculate_bonus(self,amount):
        self.salary +=self.salary*(amount/100) 
        print(self.salary)
class Developer(Employee):
    def __init__(self, name, programming_language ,salary = 0):
        self.language = programming_language
        super().__init__(name, salary)
    def get_details(self):
        print(f"name:{self.name} Programming Language :{self.language} salary:{self.salary} ")
    def calculate_bonus(self,amount):
        self.salary +=self.salary*(amount/100) 
        print(self.salary)

# Klassdan foydalanish
manager = Manager(name="Alice", salary=120000, department="Sales")
# Yangi Manager yaratildi, ism: Alice, maosh: 120000, bo'lim: Sales

developer = Developer(name="Bob", salary=100000, programming_language="Python")
# Yangi Developer yaratildi, ism: Bob, maosh: 100000, dasturlash tili: Python

manager.get_details()
# Manager: Alice, Department: Sales, Salary: 120000
developer.get_details()
# Developer: Bob, Programming Language: Python, Salary: 100000

manager.calculate_bonus(10)
# Manager uchun bonus: 12000 so'm (10%)
developer.calculate_bonus(5)
# Developer uchun bonus: 5000 so'm (5%)