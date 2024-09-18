""" Объектно ориентированное программирование """

" Наследование и множественное наследование "

class Game:
    def __init__(self, game_name, graphics, game_year, company):
        self.game_name = game_name
        self.graphics = graphics
        self.game_year = game_year
        self.company = company
        
    def info(self):
        print(f"Название игры - {self.game_name}, максимальная графика - {self.graphics}, дата релиза - {self.game_year}, создатели - {self.company}")
        
game = Game('CsGO', 'FULL HD 4K', 2013, 'Valve')
# game.info()

class Roblox(Game):
    def __init__(self, game_name, graphics, game_year, company, multiplayer):
        super().__init__(game_name, graphics, game_year, company)
        # Game.__init__(game_name, graphics, game_year, company)
        self.multiplayer = multiplayer
        self.name = 'player'
        self.gender = 'man'
        self.skin = 'VIP'
        self.hp = 100
        
    # def info(self):
    #     print(f"Название игры - {self.game_name}, максимальная графика - {self.graphics}, дата релиза - {self.game_year}, создатели - {self.company}, мультиплеер - {self.multiplayer}")
    
    def info_player(self):
        print(f"Игрок - {self.name}, Пол - {self.gender}, Облик - {self.skin}, Здоровье - {self.hp}")
        print('=========================\nROBLOX - запустился и готов к игре!')
    
    def edit_player(self):
        name = input("Введите имя игрока: ")
        gender = input("Введите пол игрока: ")
        skin = input("введите облик персонажа: ")
        self.name = name
        self.gender = gender
        self.skin = skin
    
roblox = Roblox("Roblox", 'ULTRA', '2006', 'Roblax Corporation', "Да")
# roblox.info()
# roblox.edit_player()
# roblox.info_player()

class Snake(Roblox):
    def __init__(self, game_name, graphics, game_year, company, multiplayer, name, gender, skin):
        super().__init__(game_name, graphics, game_year, company, multiplayer)
        self.name = name
        self.gender = gender
        self.skin = skin
        self.hp = 100 

snake = Snake('Snake', 'HD', '2024', 'Geeks','Нет', 'Бека', 'Муж', 'Platinium')
snake.info()
# snake.info_player()
        
        
# ''''Задание: Симуляция Зоопарка с Конструкторами
# Создайте классы, которые будут моделировать разных животных в зоопарке, используя множественное наследование и конструкторы для инициализации объектов.

# Базовые классы:

# Создайте класс Animal, который будет представлять общее животное. У этого класса должен быть конструктор __init__(), который принимает параметр name для имени животного. Также добавьте методы eat() и sleep(), которые выводят сообщения, например, "{name} ест" и "{name} спит".

# Создайте класс Walker, который будет представлять животных, которые могут ходить. У этого класса должен быть метод walk(), который выводит сообщение "{name} ходит".

# Создайте класс Swimmer, который будет представлять животных, которые могут плавать. У этого класса должен быть метод swim(), который выводит сообщение "{name} плавает".

# Создайте класс Flyer, который будет представлять животных, которые могут летать. У этого класса должен быть метод fly(), который выводит сообщение "{name} летает".

# Комбинированные классы:
                                            
# Создайте класс Penguin, который наследуется от Animal, Walker, и Swimmer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что пингвин может ходить и плавать.

# Создайте класс Duck, который наследуется от Animal, Walker, Swimmer, и Flyer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что утка может ходить, плавать и летать.

# Создайте класс Bat, который наследуется от Animal и Flyer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что летучая мышь может летать.

# Тестирование:

# Создайте экземпляры каждого из созданных вами классов, передавая им имена, и вызовите для них методы describe(), а также методы, относящиеся к их поведению (например, walk(), swim(), fly()).'''


# class Penguin(Animal, Walker, Swimer)