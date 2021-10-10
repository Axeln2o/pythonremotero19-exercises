class Client:
    def __init__(self, nume, cif, reg_com, adresa):
        self.nume = nume
        self.cif = cif
        self.reg_com = reg_com
        self.adresa = adresa


class Furnizor(Client):
    def __init__(self, nume, cif, reg_com, adresa, tel, email, cont, banca, tva, plata_tva):
        super().__init__(nume, cif, reg_com, adresa)
        self.tel = tel
        self.email = email
        self.cont = cont
        self.banca = banca
        self.tva = tva
        self.plata_tva = plata_tva


class Produs:
    def __init__(self, nume_prod, UM, cantitate, pret):
        self.nume_prod = nume_prod
        self.UM = UM
        self.cantitate = cantitate
        self.pret = pret
        # todo:fix val_tva


# class Delegat


class Factura:
    def __init__(self, client, furnizor, produs, ):
        self.client = client
        self.furnizor = furnizor
        self.produs = produs

    def afisare(self):
        print(f"{self.furnizor.nume: <30}")
        print(f"{'CIF:' + self.furnizor.cif: <30}")
        # print(f"")


furnizor = Furnizor('Ionut', 'RO50432123', 'J85/9130/8345', 'Mihai Viteazul 3, Iasi', '0749294030',
                    'nicoletaluchian@gmail.com', 'RO79BREL00055064207300100', 'Revolut', 19, True)
client = Client('Alexandru', 'RO12345678', 'J45/5469/2021', 'Bd Chimiei 7B, Iasi')
produs = Produs('Ciocolata', 'buc', 100, 50)
produs2 = Produs('suc', 'buc', 2, 10)
produs3 = Produs('seminte', 'buc', 1, 3)

produse = [produs, produs2, produs3]


