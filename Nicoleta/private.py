# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self.__name = name
#         self.__age = age
#
#     def print_details(self):
#         print(f"name: {self.__name}, age: {self.__age}")
# #
# #
# #
# # my_dog = Animal()
# # my_dog.print_details()  # Python will throw an error !!!
#
# class Animal(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property  # getter - get field value
#     def age(self):
#         return self.__age
#
#     @age.setter  # setter - sets a new field value
#     def age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be greater than 0.")
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if name == '':
#             print('Please input a name!')
#         else:
#             self.__name = name
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
# my_dog = Animal("Dog", 11)
# my_dog.age = 3  # Sets age - uses setter
# print(my_dog.age)  # Reads age - uses a getter
#
# my_dog.name = ''
# my_dog.name = 'Beni'
# print(my_dog.name)
#
#
# # del my_dog.age
# # print(my_dog.age)


class Human:
    def __str__(self):
        return f"Name:{self.name}, Height: {self.height}, Weight: {self.weight}"

    def __init__(self, name, height, weight):
        self.__name = name
        self.__height = height
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight


class Programmer(Human):
    def __init__(self, name, height, weight, languages):
        super().__init__(name, height, weight)
        self.languages = languages

    def __str__(self):
        return f"Name:{self.name}, Height: {self.height}, Weight: {self.weight}, Languages{self.languages}"


om = Human('Nicoleta', 158, 60)
programator = Programmer(1.70, 'Ioana', 55, ["Java", "C++", "Python"])

bob = Programmer("Bob", 180, 100, ["Python", "Java"])
print(bob.name)  # Access to the name field inherited from the Human class
print(om)
print(programator)
