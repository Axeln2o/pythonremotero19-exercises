class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property  # getter - get field value
    def age(self):
        return self.__age

    @age.setter  # setter - sets a new field value
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "":
            print(f'Please input name: ')
        else:
            self.__name = name

    @age.deleter
    def age(self):
        del self.__age


my_dog = Animal("Nero", 14)
print(my_dog.age)  # Reads age - uses a getter
my_dog.name = ""
my_dog.name = "Nero"

del my_dog.age
# print(my_dog.age)


class Human:
    def __init__(self, height, name, weight=57):
        self.name = name
        self.height = height
        self.weight = weight


class Programer(Human):
    def __init__(self, height, name, weight, languages):
        super().__init__(height, name, weight)
        self.languages = languages


om = Human(158, 'Laura', 60)
programator = Programer(1.70, 'Ioana', 55, ["Python", 'C++', 'Java'])

class Human:
    def __str__(self):
        return f"Name:{self.__name}, \nHeight: {self.__height}, \nWeigth: {self.__weigth} "

    def __repr__(self):
        return str(self)

    def __init__(self, name, height, weigth):
        self.__name = name
        self.__height = height
        self.__weigth = weigth

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
    def weigth(self):
        return self.__weigth

    @weigth.setter
    def weigth(self, weigth):
        self.__weigth = weigth


class Programmer(Human):
    def __init__(self, name, height, weigth, languages):
        super().__init__(name, height, weigth)
        self.languages = languages


om = Human("Corina", 162, 53)
om1 = Human("Mihai", 172, 72)
programator = Programmer("Ioana", 159, 55, ["Python", "Java"])
print(om.height, om.weigth, om.name)
print(om1)

oameni = [om, om1]
print(oameni)
