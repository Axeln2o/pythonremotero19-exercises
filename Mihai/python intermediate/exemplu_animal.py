class Animal:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.position = 0

    def eat(self, treat):
        print(f"Animal {self.name} eats treat {treat} !")

    @staticmethod
    def print_sound():
        print("This animal makes noises!")

    # o metoda statica nu depinde de o anumita
    # instanta in nici un fel (deci nu punem argumentul "self")
    @staticmethod
    def present():
        print("Aceasta este o metoda statica dintr-o clasa care reprezinta un animal!")

    def move(self):
        self.position += 1