class Entity:
    ok = True

    def __init__(self, nr_vieti, nume, putere, damage, pozitie_axa_verticala, pozitie_axa_orizontala):
        self.damage = damage
        self.nr_vieti = nr_vieti
        self.nume = nume
        self.putere = putere
        self.pozitie_axa_verticala = pozitie_axa_verticala
        self.pozitie_axa_orizontala = pozitie_axa_orizontala

    def is_alive(self):
        if self.nr_vieti > 0:
            print(f"{self.nume} este inca in viata!")
            ok = True

        else:
            print(f"{self.nume} a decedat!")
            ok = False

    def apply_damage(self, attackObj):

        self.attacker = self.nume
        self.attackerPower = self.damage
        self.victim = attackObj.nume
        self.victimHealth = attackObj.nr_vieti
        self.nr_vieti_nou = self.victimHealth - self.damage
        print(self.nume, "you have chosen to attack", self.victim)
        print(self.victim, "you have suffered", self.attackerPower, "damage and  your number of lives is now",
              self.nr_vieti_nou)
        attackObj.nr_vieti -= self.damage

    def take_damage(self, atacatorObj):
        if Entity.ok and self.nr_vieti > 0:
            self.attacker = atacatorObj.nume
            self.attackerPower = atacatorObj.damage
            self.victim = self.nume
            self.nr_vieti_nou = self.nr_vieti - atacatorObj.damage
            self.nr_vieti = self.nr_vieti_nou
            print(atacatorObj.nume, "you have chosen to attack", self.victim)
            print(
                f" me : {self.victim}, I have suffered, {atacatorObj.damage}, damage and  my number of lives is now {self.nr_vieti_nou}")
        else:
            print(f"{self.nume} is already dead! Can't be attacked !")
            Entity.ok = False

    def move_N(self):
        self.pozitie_axa_verticala += 1
        print(f"Acum pozita actuala este in : A({self.pozitie_axa_verticala} : {self.pozitie_axa_orizontala})")

    def move_S(self):
        self.pozitie_axa_verticala -= 1
        print(f"Acum pozita actuala este in : A({self.pozitie_axa_verticala} : {self.pozitie_axa_orizontala})")

    def move_E(self):
        self.pozitie_axa_orizontala += 1
        print(f"Acum pozita actuala este in : A({self.pozitie_axa_verticala} : {self.pozitie_axa_orizontala})")

    def move_W(self):
        self.pozitie_axa_orizontala -= 1
        print(f"Acum pozita actuala este in : A({self.pozitie_axa_verticala} : {self.pozitie_axa_orizontala})")

    def get_position(self):
        tupla_pozitie = (self.pozitie_axa_verticala, self.pozitie_axa_orizontala)
        return tupla_pozitie


obiect_nou = Entity(10, "Niko", 100, 3, 0, 0)
obiect_2 = Entity(10, "Niku paleru", 100, 2, 0, 0)

obiect_nou.move_S()
obiect_nou.move_W()
obiect_nou.move_S()
obiect_nou.move_S()
print(obiect_nou.get_position())
obiect_nou.move_N()
print(obiect_nou.get_position())

obiect_nou.take_damage(obiect_2)
obiect_nou.take_damage(obiect_2)
obiect_nou.take_damage(obiect_2)
obiect_nou.take_damage(obiect_2)
obiect_nou.take_damage(obiect_2)
obiect_nou.take_damage(obiect_2)
