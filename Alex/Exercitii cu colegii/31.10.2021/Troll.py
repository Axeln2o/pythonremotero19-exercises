from Entity import Entity


class Troll(Entity):
    farsa = False

    def __init__(self, nr_vieti, nume, putere, damage, pozitie_axa_verticala, pozitie_axa_orizontala, e_razbunator):
        super().__init__(nr_vieti, nume, putere, damage, pozitie_axa_verticala, pozitie_axa_orizontala)
        self.e_razbunator = e_razbunator
        if self.e_razbunator:
            Troll.farsa = True

    def fac_farse(self):
        if Troll.farsa:
            print(
                "Hahaha acest troll e razbunator si tocmai ti-a facut o farsa \n Tocmai ce ti-a trimis poze fostei tale cu actuala Opa!")
        else:
            print("Acest Troll nu stie sa faca farse....")

    def suna_la_micata(self, attackObj):
        print("Acest troll a sunat-o pe mica-ta si a zis ca vinzi droguri la mana a14!")
        print("Acum a chemat si politia la tine ")
        attackObj.nr_vieti = 0
        print(attackObj.nr_vieti)
        print(f"Numarul de vieti al {attackObj.nume} a ajuns la {attackObj.nr_vieti}")


obiect1 = Troll(1, "Garcea", 1, 2, 0, 0, 0)
obiect1.fac_farse()
obiect2 = Troll(1, "Vacanta mare", 1, 2, 0, 0, 1)
obiect1.suna_la_micata(obiect2)
