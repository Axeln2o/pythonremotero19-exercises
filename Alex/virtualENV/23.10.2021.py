"""..."""

"""..."""

"""

## Clase - sunt folosite pentru gruparea unor lucruri ce au ceva in comun
## In acelasi timp o clasa este ceva asemanator cu un string, functie etc.
## instanta = obiect = o variabila ce implementeaza o clasa
x = 5 #(int)
y = 5.5 #(flot)
s = "word" #(string)
"""
class Car:
# __init__: este o functie specifica clasei
# __init__: are scopul a initializa ceva, in cazul nostru clasa
# __init__: se apeleaza la crearea clasei, primul si primul lucru

    def __init__(self, m_model, m_an, m_horsePower):
        self.model = m_model
        self.an = m_an,
        self.horsePower = m_horsePower

# m_model, m_an (parametrii constructorului, traiesc doar in functia __init__ denumita si Constructor #

    def afiseazaModelul(self):
        print(self.model)

    def afiseazaAnul(self):
        print(self.an)

    def getKWfromHP(self):
        return self.horsePower / 1.35

car1 = Car("Audi", 2020, 150)
car2 = Car("Volvo", 2021, 202)


# Car.afiseazaAnul(car1)
# Car.__init__(car1, "Audi", 2020)

Car1 = {
"model": "Audi",
"an": 2020,
"HP": 150
}

Car2 = {
"model": "Volvo",
"an": 2020,
"HP": 150
}

def getKWfromHP(horsePower):
    return horsePower / 1.35

