from Entity import Entity


class Vampire(Entity):
    def __init__(self, nr_vieti, nume, putere, damage, pozitie_axa_verticala, pozitie_axa_orizontala):
        super().__init__(nr_vieti, nume, putere, damage, pozitie_axa_verticala, pozitie_axa_orizontala)

    def vampirism_energetic(self, attackObj):
        print("Cand esti atacat de acest vampir, te suje de energie si viata ta se scurge pana la 0")
        attackObj.nr_vieti = 0
        self.name_attackedobj = attackObj.nume
        print(f"Acum viata lui {self.name_attackedobj} este 0 !!")

    def speed(self):
        directie_deplasare = input("Dati directia pe care doriti sa se miste")
        if directie_deplasare == "w":
            self.pozitie_axa_orizontala -= 3
        if directie_deplasare == "e":
            self.pozitie_axa_orizontala += 3
        if directie_deplasare == "n":
            self.pozitie_axa_verticala += 3
        if directie_deplasare == "s":
            self.pozitie_axa_verticala -= 3

        print(f"Acum pozitia lui {self.nume} este: ")
        print(Entity.get_position(self))


obiect1 = Vampire(1000, "Tepesu", 100, 3, 0, 0)
obiect2 = Vampire(1000, "Dragulin", 100, 3, 0, 0)
obiect1.vampirism_energetic(obiect2)
print(obiect1.get_position())
obiect1.speed()
