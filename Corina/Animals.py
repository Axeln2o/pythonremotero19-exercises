class Animal(object):

    def __init__(self, name, age, colour, species):
        self.name = name  # set the default value for the name field of the Animal class object
        self.age = age
        self.colour = colour
        self.species = species

    def print_details(self):  # method for printing the state of an object
        print(f"Name: {self.name}, age: {self.age}, colour: {self.colour}, species: {self.species}")


my_dog = Animal("Bruna", 3, "maro", "caine")
my_dog.print_details()

my_cat = Animal("Tommy", 1, "gri", "pisoi")
my_cat.print_details()

