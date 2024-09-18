""" Объектно ориентированное программирование """
" Полиморфизм "

# num1 = 1
# num2 = 2

# print(num1 + num2)

# string1 = "Hello"
# string2 = "Geeks"

# print(string1 + string2)

# print(len("ООП программирование"))
# print(len(['python', 'Java', 'C#', 'Scala']))
# print(len({"python" : "Django", "JS" : "React"}))

# class Cat:
#     def __init__(self, name, preferences):
#         self.name = name 
#         self.preferences = preferences
        
#     def info(self):
#         print(f'Я кот. Меня зовут {self.name}. Мне {self.preferences} года')
    
#     def make_sound(self):
#         print("Мяу")
        
# class Dog:
#     def __init__(self, name, preferences):
#         self.name = name 
#         self.preferences = preferences
        
#     def info(self):
#         print(f'Я собака. Меня зовут {self.name}. Мне {self.preferences} года')
    
#     def make_sound(self):
#         print("Гаф")
        
# cat = Cat("Tom", 2)
# dog = Dog("Muhtar", 3)

# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()
    

class PaymentMethod:
    def pay(self, amount):
        pass 
    
class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Сумма {amount}, оплачивается по кредитной катре"
    
class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"Сумма {amount}, оплачивается по PayPal"
    
class BankTransfer(PaymentMethod):
    def pay(self, amount):
        return f'Сумма {amount}, оплачивается по банковскому переводу'
    
payments = [CreditCard(), PayPal(), BankTransfer()]

for payment in payments:
    print(payment.pay(input("Введите сумму: ")))