from Entity import Entity # Aici vedem cele 4 clase ce mostenesc clasa Entity. Mostenirea se face prin 'import'


class Orc(Entity):
    def __init__(self, nr_vieti, nume, putere, damage, pozitie_axa_verticala, pozitie_axa_orizontala):
        super().__init__(nr_vieti, nume, putere, damage, pozitie_axa_verticala, pozitie_axa_orizontala)

    def atac_letal(self, attackObj):
        self.attacker = self.nume
        self.victim = attackObj.nume
        self.victimHealth = attackObj.nr_vieti
        self.nr_vieti_nou = self.victimHealth - self.victimHealth
        print(self.nume, "you have chosen to attack", self.victim)
        print(self.victim, "you have suffered total  damage and  your number of lives is now",
              self.nr_vieti_nou)
        attackObj.nr_vieti = 0

    def ma_ascund_in_pestera(self):
        self.nr_vieti += 10
        print(f"M-am ascuns in pestera, deci m-am odihnit si am mai capatat 10 vietzi! acum am {self.nr_vieti}")


orculet = Orc(10, "Boc", 100, 2, 0, 0)
orculet2 = Orc(10, "Emil,", 100, 2, 0, 0)
orculet.atac_letal(orculet2)  # astea sunt comenzile
orculet2.ma_ascund_in_pestera()
