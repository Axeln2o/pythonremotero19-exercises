from abc import abstractmethod, ABC
#O clasa abstracta este o clasa care are cel putin o metoda abstracta


class Fruct(ABC):
    def __init__(self,nume,tip,culoare):
        self.tip=tip
        self.nume=nume
        self.culoare=culoare

    def __str__(self):
        return f"{self.nume} este un fruct de tip {self.tip} si are culoarea {self.culoare}"

    @abstractmethod
    def val_nutritive(self):
        pass


class Banana(Fruct):
    temperatura_oxidare=10
    def __init__(self,nume,tip,culoare,continut_zahar):
        super().__init__(nume,tip,culoare)
        self.continut_zahar=continut_zahar

    def iradiatii(self):
        return f"Nivelul de radiatie este: {self.continut_zahar *3}"

    @staticmethod
    def origine():
        print("Toate bananiele sunt de import!")

    @classmethod
    def oxidare(cls):
        print(f"Banana s-a innegrit la {cls.temperatura_oxidare} grade")

    def val_nutritive(self):
        print(f"Valorile nutritive sunt foarte bune la {self.nume}")



class Mar(Fruct):
    def __init__(self,nume,tip,culoare,masa):
        super().__init__(nume,tip,culoare)
        self.masa=masa

    def energie_cinetica(self,viteza):
        return (self.masa*viteza*viteza)/2

    def val_nutritive(self):
        print(f"Valorile nutritive sunt foarte bune la {self.nume}")





if __name__=="__main__":
    b=Banana("Banany","Dole","galben",12.23)
    print(b)
    m=Mar("Mar","ionatan","rosu",75)
    print(m.energie_cinetica(100))
    Banana.origine()
    Banana.oxidare()
