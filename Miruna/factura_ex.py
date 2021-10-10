class Client:
    def __init__(self, nume,cui,reg_com, adresa):
        self.nume = nume
        self.cui = cui
        self.reg_com = reg_com
        self.adresa = adresa

class Furnizor(Client):
    def __init__(self, nume,cui,reg_com, adresa, telefon, email, cont, banca,tva, plata_tva
        super().__init__(ume,cui,reg_com, adresa)
        self.telefon = telefon
        self.email = email
        self.cont = cont
        self.banca = banca
        self.tva = tva
        self.plata_tva = plata_tva
class Produs:
    def __init__(self, nume_prod, um, cant, pret):
        self.nume_prod = nume_prod
        self.um = umself.cant = cant
        self.pret = pret
        self.valoare = cant*pret
        #todo: fix val_tva

#todo class Delegat
class Factura: # aceasta clasa tb sa stie sa foloseasca celelalte clase gen Client, Furnizori
    def __init__(self, client, furnizor, produse, delegat):
        self.client = client
        self.furnizor = furnizor
        self.produse = produse
        self.delegat = delegat
    def afisare(self):
        print(f"{self.furnizor.nume:<30}")
        print(f"{"CIF: " + self.furnizor.cui:<30}")


furnizor = Furnizor("Emag", "15764", "J40/52146", "Buc", "722355413", "office@emag.ro", "RO4712300000001122334455", "BCR", 19, True)
client = Client("Andrei", "RO123456", "J41/47/2345", "Cluj")
produs = Produs("Milka", "buc", 100, 50)
produs2 = Produs("suc", "buc", 2,10)
produs3 = Produs ("seminte", "buc", 1,3)
produse = [produs, produs2, produs3]
factura = Factura(client, furnizor, produse, None)