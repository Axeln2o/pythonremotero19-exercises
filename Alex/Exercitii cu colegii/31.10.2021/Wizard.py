from Entity import Entity  # Aici vedem cele 4 clase ce mostenesc clasa Entity. Mostenirea se face prin 'import'


class Wizard(Entity):
    def __init__(self, nr_vieti, nume, putere, damage, pozitie_axa_verticala, pozitie_axa_orizontala):
        super().__init__(nr_vieti, nume, putere, damage, pozitie_axa_verticala, pozitie_axa_orizontala)

    def cast_spell(self):  # When this spell is used, the player who is spelled, will reach the position 0, 0
        self.pozitie_axa_orizontala = 0
        self.pozitie_axa_verticala = 0

    def vraja_malefica(self):
        self.nume = "Suparici"
        print(f"Muhaha haha ha Evil Laugh! I have cursed you and now your name is {self.nume} Muhaha hahaha ")
        self.nr_vieti = 0
        print(
            f"De asemenea, deoarece ai fost blestemat sa ai un nume penal, si numarul de viati a ajuns la {self.nr_vieti}! ")


obiect1 = Wizard(10, "Dr House", 10000, 1, 0, 0)
obiect1.move_N()
obiect1.move_N()
obiect1.cast_spell()
print(obiect1.get_position())
print(obiect1.nume)
print(obiect1.nr_vieti)
