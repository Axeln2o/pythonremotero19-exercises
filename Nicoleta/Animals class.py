class Animal:
    name = ""  # class variable
    age = 0  # class variable

    def __init__(self, name, age, colour, species):
        self.name = name  # set the default value for the name field of the Animal class object
        self.age = 2
        self.colour = colour
        self.species = species

    def print_details(self):  # method for printing the state of an object
        print(f"Name: {self.name}, age: {self.age}, colour: {self.colour}, species: {self.species}")


my_cat = Animal("Freya", 2, "gri", "pisica")
my_cat.print_details()

my_dog = Animal("Liza", 5, "portocaliu", "caine")
my_dog.print_details()

