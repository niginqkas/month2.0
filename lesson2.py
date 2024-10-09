# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f'Name: {self.name}, Age: {self.age}, Birth Year: {2024 - self.age}
#
#
# some_animal = Animal('Anim', 3)
# some_animal.age = -2
# print(some_animal.info())
#
#
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.__name
#
#     def info(self, name):
#         self.__name = name
#
#     def info(self):
#         return f'Name: {self.name}, Age: {self.age} Birth Year: {2027 - self.age}'
#
#
#
# class Cat (Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         super(Cat, self).__init__(name, age)
#
#
# class Dog(Animal):
#     def __init__(self, name, age, commands):
#         super(Dog, self).__init__(name, age)
#         self.commands = commands
#
#     @property
#     def commands(self):
#         return self.__commands
#
#     @commands.setter
#     def commands(self, commands):
#         self.__commands = commands
#
#
# cat = Cat('Tom', 2)
# print(cat.info())
#
# dog = Dog('Sharik', 10)
# print(dog.info())
#
#
#
# class FightingDog(Dog):
#     def __init__(self, name, age, commands, wins):
#         super(FightingDog, self).__init__(name, age, commands)
#         self.wins = wins
#
#     @property
#     def wins(self):
#         return self.__wins
#
#     @wins.setter
#     def wins(self, value):
#         self.__wins = value



class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")

    def info(self):
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")



class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}")



class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.length * self.width

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.length}{self.unit}, width: {self.width}{self.unit}, area: {area}{self.unit}")



figures = [
    Square(5),
    Square(7),
    Rectangle(5, 8),
    Rectangle(10, 2),
    Rectangle(3, 4)
]


for figure in figures:
    figure.info()

