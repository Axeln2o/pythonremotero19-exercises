

from Intermediate_exercitiu_1 import Animal

# Clasa Mamma mosteneste clasa Animal, adica nume, varsta, culoare, dar poate avea mult mai multe


class Mammal(Animal):

    def __init__(self, name, age, colour, weight):
        super().__init__(name, age, colour)  # aici se va inializa 'init-ul' din clasa Animal din exercitiul celalalt
        self.weight = weight

    def run(self):
        print(f"Mammal named {self.name} is running! Its weight is  {self.weight} kg!")

    def eat(self, treat):
        print(f"Mammal {self.name} eats treat {treat} and weighs {self.weight}! >")

    def move(self):
        super().move()
        self.position += 2  # aici are legatura iar cu Move: a facut 1 de pe pagina cealalta + 2 de aici si a zis position dupa first move este 3
if __name__ == "__main__":  # aceasta este o conventie standard din python care se scrie cand vrem sa facem ce am facut mai jos
    m = Mammal("Leo", 4, "yellow", 150)
    m.run()

    print("\n===========\n")

    m.eat("meat")

    m.move()
    print(f"Position after first move is: {m.position}")  # da 3

    m.move()
    print(f"Position after second move is: {m.position}")  # da 6

    print(isinstance(m, Mammal))  # este m de tip Mammal? Da, pt ca m este instantiat ca Mammal
    print(isinstance(m, Animal))  # este m de tip Animal? Da, pt ca Mammal mostenenste Animal

    print(issubclass(Mammal, Animal)) # este Mammal o subclasa a lui Animal? Da, pt ca Mammal mosteneste Animal

    # facem o lista cu animale
    animals_list = []
    # primul adaugat va fi m, instanta a Mammal
    animals_list.append(m)
    # mai adaugam un nou obiect a, de tip Animal
    a = Animal("generic", 5, "abc")
    animals_list.append(a)

    # iteram si tratam toate obiectele ca fiind de tip Animal
    for animal in animals_list:
        animal.move()
        animal.eat("ceva")
        print("-------------------")
