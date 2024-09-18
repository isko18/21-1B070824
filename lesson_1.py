""" Объектно ориентированное программирование """

# full_name = 'Аслан' #Змеиный регистр

# FullName = 'Жибек' #Верблюжий регистр



class Car: #шаблон или же чертеж
    def __init__(self,marka, model, color): #__init__ (магический метод) контруктор
        #Атрибут объекта
        self.marka = marka
        self.model = model # self (ссылка на текущий объект)
        self.color = color 
        #Атрибут класса
        self.bak = 0.1
        self.is_start = False
        
    def info(self):
        print(f"Марка машины - {self.marka}, модель - {self.model}, цвет - {self.color}")
        
    def start(self):
        if self.bak > 0:
            self.is_start = True
            print(f"Машина {self.marka} - {self.model} заведена")
        else:
            print(f"Машина {self.marka} - {self.model} нет топлива")
            
    def stop(self):
        self.is_start = False
        print(f"Машина {self.marka} - {self.model} заглушено")
        
    def drive(self, city):
        if self.is_start == True:
            print(f"Машина {self.marka} - {self.model} едет в {city}")
        else:
            print(f"Машина {self.marka} - {self.model} не заведена ")
            21
        
bmw = Car('BMW', 'M5 F90', 'black')
bmw.info()
bmw.start()
# bmw.stop()
bmw.drive("Дубай")

""" Создать класс (Book).Передать параметры (avtor, book_name, year). Создать метод info. Вызвать переданный аргумент """