class Client:
    def __init__(self, name, cif, j, adress):
        self.name = name
        self.cif = cif
        self.j = j
        self.adress = adress

    def print_details(self):
        print(f"Name: {self.name}, cif: {self.cif}, j: {self.j}, adress: {self.adress}")



class Furnizor(Client):
    def __init__(self, name, cif, j, adress, email, cont, banca):
        super().__init__(name, cif, j, adress)
        self.email = email
        self.cont = cont
        self.banca = banca


class Produs:
    def __init__(self, nume_prod, um, cant, pret):
        self.nume_prod = nume_prod
        self.um = um
        self.cant = cant
        self.pret = pret
        self.valoare = (cant * pret)


#          todo: fix val_tva
class Factura:
    def __init__(self, client, furnizor, produse, delegat):
        self.client = client
        self.furnizor = furnizor
        self.produse = produse
        self.delegat = delegat

    def afisare(self):
        print(f"{self.furnizor.nume: <30}")



furnizor = Furnizor("gru," "RO65656565", "j/19/20056455", f'Baladei 1' 'skjkj@njnas.com', 'ROINGB000121212120000',
                    'Villain`s Bank', 19, True)
client = Client("Minions", "RO05255555", "j40/254/25544", f"Nordului 2")
produs = Produs("The moon", "buc", 1, 100000000545)
produs2 = Produs("Freeze gun", "buc", 3, 4900000)
produse = [produs, produs2]

factura = Factura(client, furnizor, produse, None)
