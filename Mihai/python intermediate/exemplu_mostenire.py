from exemplu_animal import Animal


# clasa Mammal mosteneste clasa Animal

class Mammal(Animal):

    registry=[] #Am creat o lista gola, cu denumirea "registry" in care urmeaza sa stochez
                #fiecare obiect creat, rand pe rand, la creearea lui!

    nr_obiecte_create = 0
    def __init__(self, name, age, color, weight):
        super().__init__(name, age, color)
        self.weight = weight
        self.registry.append(self) #Stocarea obiectelor se petrece la aceasta linie de cod!!!
        Mammal.nr_obiecte_create += 1


    def run(self):
        print(f"Mammal named {self.name} is running! Its weight is {self.weight} kg!")

    def eat(self, treat):
        #print(f"< Mammal {self.name} eats treat {treat} and weighs {self.weight}! >")
        super().eat(treat)
        print(f"This animal is a mammal and weighs {self.weight} kg!")

    def move(self):
        super().move()
        self.position += 2



if __name__ == "__main__":

    m = Mammal("Leo", 4, "yellow", 150)
    m.run()

    print("\n=====================\n")

    m.eat("meat") #"m" este obiectul !!!! ".eat" este metoda apelata "meat" este argumentul pasat ca parametru
    l=[]
    l.append(m)
    a=Animal("generic",5,"blue")
    l.append(a)

    print("\n=====================\n")

    m.move()
    print(f"Position after first move is: {m.position}")

    m.move()
    print(f"Position after second move is: {m.position}")

    print(isinstance(m,Animal))
    print(isinstance(m,Animal))
    print(issubclass(Mammal,Animal))
    print(l)
    for animal in l:
        animal.move()
        animal.eat("ceva")
        print("-----------------")

    m2=Mammal("mihai",13,"bej de baia mare",90)

    m3=Mammal("korina",23,"verde ca copacu de mesteacan",52)

    m4=Mammal("Korinutz",22,"alba ca zapada!",51)

    m5=Mammal("Alexa",13,"alba ca metilu'",68)
    m6=Mammal("Klau",12,"rozosina",69)
    for objects in Mammal.registry:
        print(objects)
        print(objects.name)
        print(objects.age)
        print(objects.color)


    print(f"Pana acum s-au creat {Mammal.nr_obiecte_create} instante ale clasei Mammal!")
    m6.print_sound()


