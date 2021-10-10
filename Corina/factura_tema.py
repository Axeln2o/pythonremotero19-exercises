class Client:
    def __init__(self, nume, cif, reg_com, adresa):
        self.nume = nume
        self.cif = cif
        self.reg_com = reg_com
        self.adresa = adresa

class Furnizor(Client):
    def __init__(self, nume, cif, reg_com, adresa, telefon, email, cont, banca, plata_tva):
        super().__init__(nume, cif, reg_com, adresa)
        self.telefon = telefon
        self.email = email
        self.cont = cont
        self.banca = banca
        self.plata_tva = plata_tva

class Produs:
    def __init__(self, nume_prod, um, cant, pret):
        self.nume_prod = nume_prod
        self.um = um
        self.cant = cant
        self.pret = pret
        self.valoare = cant * pret
        #todo: fix val_TVA
        #todo: class Delegat
class Factura:
    def __init__(self, client, furnizor, produse, delegat):
        self.client = client
        self.furnizor = furnizor
        self.produse = produse
        self.delegat = delegat
    def afisare(self):
        print(f"{self.furnizor.nume: <30}")
        print(f"{'CIF:' + self.furnizor.cif: <30}")
        # print(f"")

furnizor = Furnizor("Ionut", "RO200157", "J24/25/1995", "Oradea, Calea Clujului, nr.43", "+04720020057", "mediu@atp-exodus.com", "ROBTRL000000000X", 19, True)
client = Client("ATP MOTORS", "RO789002", "J24/12/2012", "Baia Mare, Bd. Bucuresti, nr 34")
produs = Produs("ciocolata_milka", "buc", 100, 50)
produs2 = Produs("suc", "buc", 2, 10)
produs3 = Produs("seminte", "buc", 1,3)

produse = [produs, produs2, produs3]

factura = Factura(client, furnizor, produse, None)
factura.afisare()






