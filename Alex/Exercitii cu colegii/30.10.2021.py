import random

class Agression:
    def __init__(self, trigger, caracteristici, manifestari):
        self.trigger = trigger
        self.caracteristici = caracteristici
        self.manifestari = manifestari

    def male_agression(self):
        print(f" {self.caracteristici} could be a male attribute as a sighn of agression")

    def female_agression(self):
        print(f" {self.trigger} this can trigger a female to react")

    def human_reactions(self):

        a = input("Give first reaction: ")

        b = input("Give second reaction: ")

        c = input("Give third reaction: ")

        x = random.randrange(1, 4)

        if x == 1:
            print(f"this person tends to react by {a}")

        elif x == 2:
            print(f"this person tends to react by {b}")

        elif x == 3:
            print(f"this person tends to react by {c}")





agression1 = Agression("yelling", ["nervos", "ranit", "impulsiv"], ["violenta verbala", "violenta fizica", "tipete"])
agression2 = Agression("violent look", ["agressiva", "passiva", "activa"], ["throw things", "hit the wall", "punch in the face"])
agression3 = Agression("lack of money", ["tristete", "talharie"], ["furt", "obsessiv callls"])

agression1.female_agression()
agression2.male_agression()
agression3.human_reactions()