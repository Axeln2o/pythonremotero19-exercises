class Human:
    def __str__(self):
        return f"Name:{self.name}, \nHeight: {self.height}, \nWeigth: {self.weigth} "

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

    def __str__(self):
        return f"Name:{self.name}, \nHeight: {self.height}, \nWeigth: {self.weigth}, \nLanguages:{self.languages}"


om = Human("Corina", 162, 53)
om1 = Human("Mihai", 172, 72)
programator = Programmer("Ioana", 159, 55, ["Python", "Java"])

print(om.height, om.weigth, om.name)
print(om1)

oameni = [om, om1]
print(oameni)

print(programator)


# mostenire multipla
class Bat:
    pass


class Man:
    pass


class Batman(Bat, Man):
    pass  # dupa : trebuie sa punem pass daca nu scriem nimic.
