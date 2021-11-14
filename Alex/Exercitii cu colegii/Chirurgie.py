class Medicine:
    def __init__(self, clasica, alternativa):
        self.clasica = clasica
        self.alternativa = alternativa
    def chirurgie(self):
        return(f"Tipul medicinei studiat este {self.alternativa}")
    def set_importance(self):
        self.alternativa = "actuala"


incizia = Medicine("ortopedie", "kiropractor")
print(incizia.chirurgie())
incizia.set_importance()
print(incizia.alternativa)

