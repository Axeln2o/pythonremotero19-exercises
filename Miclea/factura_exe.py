class Client:
    def __init__(self, nume, cif, rec_com, adresa):
        self.nume = nume
        self.cif = cif
        self.rec_com = rec_com
        self.adresa = adresa

class Furnizor(Client):
    def __init__(self,nume, cif, rec_com, adresa, tel, mail, cont, banca, tva, plata_tva):
        super().__init__(self, nume, cif, rec_com, adresa)
        self.tel = tel
        self.mail = mail
        self.cont = cont
        self.banca = banca
        self.tva = tva
        self.plata_tva = plata_tva

class Produs:
    def __init__(self, nume_prod, um, cant, pret):
        self.nume_prod = nume_prod
        self.um = um
        self.cant = cant
        self.pret = pret
        self.valoare = cant * pret
        # todo: fix val_tva
# todo : class Delegat

class Factura:
    def __init__(self, client, furnizor, produse, delegat):
        self.client = client
        self.furnizor = furnizor
        self.produse = produse
        self.delegat = delegat
    def afisare(self):
        print(f"{self.furnizor.nume: <30}")
        print(f"{'CIF: '+ self.furnizor.cif: <30}")
furnizor = Furnizor('Ionut', 'Ro32457328', 'J84/4321/432', 'Str. Lui JIJI, nr45', '0495668523', 'cdhsuaic@yahoo.com', 'Ro 35BTRIL548359473XX', 'BT', 19, True)
client = Client('Andrei', 'Ro12343243', 'J35/4321/4321', 'Bd. Repl. nr 3')
produs = Produs('ciocolata_miklka', 'buc', 100, 50)
produs2 = Produs('cola', 'buc', 2, 45)
produs3 = Produs('seminte', 'buc', 56, 43)

produse = [produs, produs2, produs3]
# obiectul este instanta unei clase

factura = Factura(client, furnizor, produse, None)
factura.afisare()