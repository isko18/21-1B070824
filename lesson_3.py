""" Объектно ориентированное программирование """
" Инкапсуляция "

#Публичный
class PublicExample:
    def __init__(self, value):
        self.value = value # Публичный атрибут
        
    def info(self):
        return self.value #Публичный метод 
    
public = PublicExample(42)
print (public.info()) #Вызов публучного метода
print (public.value) #Публичный атрибут



#Защищенный
class ProtectedExample:
    def __init__(self, value):
        self._value = value #Защищенный атрибут    
        
    def _info(self):
        return self._value #Защищенный метод
    
protected = ProtectedExample(50)
print(protected._info()) # Это работает, но это противоречит принципам инкапсуляции
print(protected._value) # Можно получить значение напрямую, но это не рекомендуется 


#Приватный
class PrivateExample:
    def __init__(self, value):
        self.__value = value #Приватный атрибут
        
    def __info(self):
        return self.__value #Приватный метод
    
    # def accesss_private(self):
    #     return self.__info() # Публичный метод, где мы получаем доступ к приватному атрибуту
    
private = PrivateExample(300)
#Прямой вызов приватного метода вызовит ошибку
# print(private.__info())

#Прямой вызов приватного атрибута вызовит ошибку
# print(private.__value)

#Доступ через публичный метод
# print(private.accesss_private())

#Доступ к приватному атрибуту через (name mangling)
print(private._PrivateExample__value)


class MobileLegends:
    def __init__(self, person, rang, item, history):
        self.person = person #Публичный
        self.rang = rang #Публичный
        self._item = item #Защищенный
        self.__history = history #Приватный

    # def player_info(self):
    #     print(f'Персонаж - {self.person}, Ранг - {self.rang}, Сумка - {self._item}')
        
    def _item_player(self):
        peron = input("Выберите персонажа: ")
        rang = input("Введите ранг: ")
        bag = input("Введите предметы: ")
        self.person = peron
        self.rang = rang
        self._item = bag
        
    def __history_player(self):
        print(f'Персонаж - {self.person}, Ранг - {self.rang}, Сумка - {self._item}, История - {self.__history}')
        
    def acces(self):
        return self.__history_player()

    
mobile = MobileLegends('НАНА', 'Легенда', 'Облик .....', '-6 звезд (')
print(mobile._item_player())
print(mobile.acces())

  