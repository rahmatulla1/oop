import json
import os

class BasicMove:

    def __init__(self,products ,balance):
        self.products = products
        self.balance = balance

    def writeJSON(self,thing):
        with open ("drugs.json","w")as file:
            json.dump(thing,file,indent=4)

    def chek_drug(self,name,price,quantity)-> dict:
        if name in self.products.keys():
            self.products[name]["price"] = price
            self.products[name]["quantity"] += quantity
        else :
            self.products[name] = {"quantity":quantity,"price":price}
        return self.products


    def sellDrug(self,drug,quantity,):
        total=quantity*self.products[drug]["price"]
        self.products[drug]["quantity"]-=quantity
        self.writeJSON(self.products)
        return total



class UserMove:
    def __init__(self):
        with open("balance.json") as file:
            self.balance = json.load(file)
        with open("drugs.json") as file:
            self.products = json.load(file)
        self.chek = BasicMove(self.products,self.balance)

    def add_medicine(self):
        drug_name = input("dori nomi :")
        drug_price = int(input("dori narxi :"))
        drug_quantity = int(input("nechta :"))
        self.products = self.chek.chek_drug(drug_name,drug_price,drug_quantity)
        self.chek.writeJSON(self.products)
        os.system("cls")
        print("Dori muvafaqiyatli qo'shildi")


    def medicine_about(self):
        for key,value in self.products.items():
            print(f"{key} - {value["price"]:,}so'm  {value["quantity"]} dona")

            
    def sell_medicine(self,drug,quantity):
        if drug in self.products.keys():
            if quantity <= self.products[drug]["quantity"]:
                balance = self.chek.sellDrug(drug,quantity)
                self.balance["balance"] = balance
                with open("balance.json","w") as file:
                    json.dump(self.balance,file,indent=4)
            else:
                print(f"bizda {drug}dan {self.products[drug]["quantity"]} qoldi")
                # shu yerda while aylantirb yana qayta so'rasa bo'lardi yozgani erindim
        else:
            print("bizda bunday dori yo'q")


    def remove_drug(self,name):
        if name in self.products.keys():
            self.products.pop(name)
            self.chek.writeJSON(self.products)
            print("Dori o'chirildi")
        else:
            print("bunday dori yo'q")


    def update_drug_price(self,name,price):
        if name in self.products.keys():
            self.products[name]["price"] = price
            self.chek.writeJSON(self.products)
        else:
            print("bunday dori yo'q")


    def check_rest_drug(self,name):
        if name in self.products.keys():      
            return self.products[name]["quantity"]
        else:
            print("bunday dori yo'q")


    def total_medicines_value(self):
        summa = 0
        for drug in self.products:
            summa+=self.products[drug]["price"]*self.products[drug]["quantity"]
        return summa


class Pharmacy:
    def __init__(self,pharmacy_name,pharmacy_address):
        self.pharmacy_name= pharmacy_name
        self.pharmacy_address= pharmacy_address


    def menu(self):
        while True:
            print("1. Dori Qo'shish:")
            print("2. Dorilar Haqida Ma'lumot:")
            print("3. Dori Sotish:")
            print("4: Dori O'chirish:")
            print("5. Dori Narxini Yangilash:")
            print("6. Dori Zaxirasini Tekshirish:")
            print("7. Jami Dorilar Qiymatini Hisoblash:")
            print("0. Chiqish")
            choise = int(input("tanlang >> "))
            try :
                if -1>choise<8 :
                    raise Exception ("iltimos to'g'ri kiriting(1\7)")
            except (Exception,ValueError) as error:
                print(error)
            else:
                return choise
            
                
    def basic_move(self):
        move = self.menu()
        user = UserMove()
        while True:
            if move == 1:
                user.add_medicine()
            elif move == 2:
                os.system("cls")
                user.medicine_about()
            elif move == 3:
                name_drug = input("nomi :" )
                quantity_drug = int(input("qancha :" ))
                user.sell_medicine(name_drug,quantity_drug)
            elif move == 4:
                name_drug = input("nomi :" )
                user.remove_drug(name_drug)
            elif move == 5:
                name = input("nomi :")
                price = int(input("narxi :"))
                user.update_drug_price(name,price)
            elif move == 6:
                name = input("nomi :")
                print(user.check_rest_drug(name))
            elif move == 7:
                print(f"{user.total_medicines_value():,} so'm")
            else:
                exit()


p1 = Pharmacy("cs","tt")
p1.basic_move()