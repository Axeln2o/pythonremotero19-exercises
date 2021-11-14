import time  ## am pus 'import time' la finalul exercitiului, asta doar pentru a putea sa importam ceva in fisierul nou creat ''...exercitiu_2'


class Animal:

    def __init__(self, name, age, colour,):
        self.name = name
        self.age = age
        self.color = colour  # pana aici totul este standard si se face ori de cate ori definim o clasa, orice clasa, e un fel de copy-paste
        self.position = 0  # randul asta l-am scris cand am facut 'super.move'


    def eat(self, treat):  #asta este ceva ce poate face animalul
        print(f"Animal {self.name} eats treat {treat} !")


    def move(self):
        self.position += 1  # asta am folosit-o la super.move si de aici el stie ca trebuie sa mute cu '1'

    print("===============")

    @staticmethod  # acesta este un 'decorator' - aici l-am pus ca sa ajutam python-ul sa inteleaga ca mai jos nu am pus 'self' in paranteze
                    # pentru ca am vrut ca 'def present()' sa fie o 'metoda'
    def present():           # asta este ceva ce iarasi nu era in exercitiul initial, este ceva ce am adaugat abia dupa ce am preat fisierul al doiela si am dat 'import'
                                 # o metoda 'statica' nu depinde de o anumita instanta 'self', nu trebuie sa mai scriem argumentul 'self'

        print("Aceasta este o metoda statica dintr-o clasa care reprezinta un animal")

    # punctul de intrare in program


if __name__ == "__main__":   # aceasta este o conventie standard din python care se scrie cand vrem sa facem ce am facut mai jos

    Animal.present()    # asta am adaugato si mai tarziu, abia dupa ce am pus 'decoratorul @staticmethod
    print("===============")
    a = Animal("Zoro", 5, "yellow")  # aici sunt atributele animalului, il putem descire in functie de nume, varsta si culoare
                                     # spunem ca a = cu un animal cu numele, varsta si culoarea

    a.eat("fruit")                   # aici spunem ca 'a', adica animalul, mananca fructe - se scrie 'a.eat'
    print("===============")         # am printat aceste egaluri doar pentru a face o delimitare intre doua comenzi diferite

    treats_list = ["mango", "milka", "carrot", "mancare la plic", "taitei"]

    i = 0   # modifica aici "0" ca sa vezi ce se intampla dupa ce dai print

            # "i" este obiectul din lista si dupa cum am invatat are pozitia de la zero la ultimul obiect

    while i < len(treats_list):
        a.eat(treats_list[i])  # [i] este ori 'mango' ori 'carrot'  ori ...
        i += 1  # cand ii dau '+1' ef va afisa 'i=0', apoi se intoarce si face '+1' si atunci 'i=1', apoi se intoarce si face '+1' si atunci 'i=2'.
                # Se va opri la 'i = 5' pentru ca in lista noastra avem doar 5 obiecte. [mango, milka, carrot, mancare la plic, taitei],
                # si noi i-am spus sa afiseze while i < lungimea (treat_list)

        time.sleep(1)   # asta este ceva ce am pus la final, odata cu creerea comenzi de sus de tot 'import time'
                        # pentru ca am pus asta, cand dau print, imi printeaza unul dupa altul la interval de o secunda
                        # daca scot time.sleep(1), imi afiseaza totul direct, fara sa printeze in ordine si cu 1 secunda intre
                        # time si sleep sunt niste module si functii predefinite in python, time = modul, sleep = functie
    print("Finished eating!")
