# class Animal(object):# mostenire din Python, este by default chiar daca nu trecem object
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
#     @age.deleter #delete the field
#     def age(self):
#         del self.__age
#
# my_dog = Animal("Dog", 11)
# my_dog.age = 10
# print(my_dog.age)
# del my_dog.age
# print(my_dog.age)

class Human:
    def __init__(self, name, height, weight):
        self.__name = name #facem variabila privata cu __
        self.__height = height
        self.__weight = weight
        # pt a face o variabila optionala ii dai efectiv o valoare
        # cand e trecut cu nume efectiv de variabila atunci este variabil

    @property
        def name(self):
        return self.__name
    @name.setter
        def name(self, name):



class Teacher(Human):
    def __init__(self, name, height, weight, experience):
        super().__init__(name, height, weight)  # il apelez pe mostenitor prin metoda super
        self.experience = experience


om = Human("John", 158, 70)  # instantiere obiecte inseamna a defini/construi un obiect
profesor = Teacher("Mary", 175, 80, 15)
print(profesor.name)


