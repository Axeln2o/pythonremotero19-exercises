#3 capabilitati : zbor,alergare,inot

#peste: sa inoate
#caine:alergare, inot
#rate : alergare,inot,zbor
from abc import abstractmethod,ABC


class Zburator(ABC):
    @abstractmethod
    def zboara(self):
        pass

class Alergator(ABC):
    @abstractmethod
    def alearga(self):
        pass


class Inotator(ABC):
    @abstractmethod
    def inoata(self):
        pass

class Caine(Alergator,Inotator):
    def __init__(self,nume):
        self.nume=nume

    def alearga(self):
        print(f"Cainele {self.nume} alearga afara!")


    def inoata(self):
        print(f"Cainele {self.nume} inoata in lac!")




class Rata(Alergator,Inotator,Zburator):
    def __init__(self,rasa):
        self.rasa=rasa

    def alearga(self):
        print(f"Rata tip {self.rasa} alearga grabita!")

    def inoata(self):
        print(f"Rata tip {self.rasa}  inoata pe lac!")

    def zboara(self):
        print(f"Rata tip {self.rasa} zboara pe ceruri!")



if __name__=="__main__":
    c=Caine("Bobitza")
    c.inoata()
    c.alearga()
    r=Rata("Rata de rasa nobila")
    r.inoata()
    r.alearga()
    r.zboara()




