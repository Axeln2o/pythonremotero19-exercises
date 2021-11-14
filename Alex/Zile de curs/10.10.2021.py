character_name = "Tom"  #Variable - este un parametru ce poate aparea de nenumarate ori in cadrul unui cod si poate fi identificat usor sau schimbat daca este definit ca variabila.
character_age = "50"  #Variable
is_male = False

print("There once was a man named " + character_name + ",")
print("He was " + character_age + " years old.")

character_name = "Jerry"

print("He really liked the name " + character_name + " , ")
print("But didn't like being " + character_age + " . ")

my_name = "Nicolae Alexandru Gheorghe"  #Variable

print(my_name.upper())  #Fi atent ca aici dupa `upper` mai pui doua paranteze
print(my_name.lower())  #Fi atent ca aici dupa `lower` mai pui doua paranteze
print(my_name.upper().isupper()) # Aici ii cer sa imi spuna daca `upper` este `upper` si imi spune `True`, pentru ca este adevarat.
print(my_name.upper().islower()) # Aici ii cer sa imi spuna daca `upper` este `lower` si imi spune `False`, pentru ca nu este adevarat.


device_colour = "red"  #Variable
device_screen_size = "6.7 inch"  #Variable
processor_specification = "888"  #Variable
battery_capacity = "5000 mAh"  #Variable

print("My phone colour is " + device_colour + " , ")  #String with Variable
print("and the screen size is " + device_screen_size + ". ")
print("My phone's processor spec. is Snapdragon " + processor_specification + ", and ")
print("the battery capacity is " + battery_capacity + ". ")
print(device_colour.isupper())  # Functie - afirmatie de verificare, imi va raspunde cu True sau False in functie de ceea ce eu am afirmat.
print(device_colour.islower())  # Functie - afirmatie de verificare, imi va raspunde cu True sau False in functie de ceea ce eu am afirmat.

parameter_1 = "weather"  #Variable
date = "today"  #Variable
parameter_1_attribute = "cloudy"  #Variable
day_time = "evening"  #Variable
print(day_time.index("e"))
print(day_time.index("v"))
abc = "Giraffe Academy"

print(abc.index("G"))
print(abc.index("Acad")) # Imi va da rezultat nr. 8, pentru ca `A` este a opta litera; imi spune doar de unde incepe `Acad`, nu imi da informatii despre toate cele 4 litere.

print(abc.replace("Giraffe", "Elephant"))

print(" The " + parameter_1 + " " + date + " is " + parameter_1_attribute + " and I don`t like it. ") # Concatenation example - adica introduc ghilimele si o variabila intr-un text deja existent
print(" I hope by the " + day_time + " the moon will be visible. ") # Concatenation example

print(" The " + parameter_1 + " " + date + " is " + parameter_1_attribute + " and I don`t like it. ") # Concatenation example
print(" The " + parameter_1 + ")")

phrase_3 = "\"Ce te legeni, codrule,\n Fara ploaie, fara vant,\n Cu crengile la pământ?\n - De ce nu m-aş legăna, \nDacă trece vremea mea!\""

print( " \"Ce te legeni, codrule,\n Fara ploaie, fara vant,\n Cu crengile la pământ?\n - De ce nu m-aş legăna, \nDacă trece vremea mea!\"")  #Using "\n" pentru a scrie unul sub altul

## Se poate folosi \" pentru a introduce ghilimele, altfel nu se pot folosi ghilimele pentru ca ele sunt folosite cu alt scop in Python.

phrase = " Aliax Engineering"  # Inainte de `Aliax` am pus spatiu pentru ca altfel mi-l afiseaza fara alineat.
         #012345
print(phrase[0])  # `[0]` este numarul literei din cadrul variabilei `phrase`, dar in cazul de fata acea litera nu este o litera ci este un spatiu(alineatul), asa ca dupa ce dau `run`, imi afiseaza acel spatiu.
print(phrase[5])  # `[5]` este numarul literei din cadrul variabilei
print(phrase + " is my first LTD. ")  # Concatenation example - Take a string and append another string to it.

phrase_1 = "is"
print(" Aliax Engineering " + phrase_1 + " my first LTD")  #Concatenare
print(len(phrase_1))
print(f"Lungimea stringului este: {len(phrase_1)}")  # Nu stiu inca exact de ce am folosit `f` si care e legatura cu acoladele.
print(len(phrase_3))
print(phrase_1[0])  # observ ca functia parantezei patrate este sa imi arate o informatie din interiorul variabilei.
print(phrase_1[1])



aa = " Astazi este Duminica. "
ab = " Tot astazi este si prima zi cand lucrez individual in Python. "
ac = " Am ajuns la concluzia clara ca daca nu lucrez individual, nu am nici o sansa sa inteleg programul. "
ad = " Trebuie sa am tot timpul in minte scopul pentru care am inceput acest curs. "
ae = " Scopul clar este:"
af = " crearea acelei oportunitati ce imi va permite la un moment dat in viitor sa lucrez de acasa. "
ag = " Trebuie tinut cont si de faptul ca domeniul IT este un domeniu ce va putea oferi un job in viitor, viitor in care foarte multe meserii vor disparea, fiind inlocuite de roboti. "

print(len(ag))

print(" Textul pe care l-am gandit acum pe moment este:" + aa +" \n" + ab + " \n" + ac + " \n" + ad + " \n" + ae + "" + af + " \n" + ag + ")")

print("The length of the string is:", (len(ag)))
print(f"The length of the string is: {len(ag)}")

x = 1
y = 2
z = 3

print(x, y, z)  #aici si la urmatoarele doua am facut eu un experiment pentru a vedea cum afiseaza in functie de parantezele folosite.
print([x], [y], [z])
print([x] + [y] + [z])

print(2.0987)
print(-2.0987)
print(3 + 4.5)
print(3 - 4.5)
print(3 * 4.5)
print(3 * (4 + 5))
print(10 % 3)
my_num = 5
print(my_num)
print(str(my_num))
print(str(my_num) + " is my favourite number")
print(my_num)
my_num = -5
print(abs(my_num))  # functia `abs` - absolute number, numarul absolut al lui -5 este 5.
print(pow(3, 2))  # functie de ridicare la putere, il ridica pe 3 la putearea a doua
print(pow(3, 4))   # 3 la a patra = 81
print(max(4, 6))    # afiseaza cel mai mare numar
print(min(4, 6))    # minimul din cele doua
print(round(3.2))   # functie care rotunjeste un numar
print(round(3.8))

from math import *   # `math`` este un `module`; pentru a avea acces la functii mai complexe, trebuie sa scriem acest enunt

my_num = -5
print(floor(3.7))  # aici rotunjeste catre cel mai mic numar
print(ceil(3.7))   # aici rotunjeste in sus, ceva de genul functiei `round`
print(sqrt(36))    # aici `sqrt` extrage radacina patrata

 # Get `input` from a user - it will allow a user to input information into our program

#input("enter your name: ")
#name = input("enter your name: ")  # `name` este o variabila; userul va introduce numele si eu ii voi afla astfel numele
#age = input("enter your age: ")
#print("Hello " + name +"!")
#print("Hello " + name + "! You are " + age)  # deci programul a obtinut informatia de la user si apoi a fost capabil sa ii spuna `Hi user, you`re age is ...; cred ca asta este un algoritm, nu?

             #Building a basic calculator
 # In principiu incercam sa facem o operatie de adunare, sau, userul sa faca pentru ca el scrie `input` si Python ofera rezultatul
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = num1 + num2  # Aici nu a dat cum trebuie - a dat 45, cand num1 = 4 si num2 = 5
#result = int(num1) + int(num2)  # Aici in schimb, pentru ca am folosit functia `int` = `integer numnber`, mi-a facut calculul corect si mi-a dat rezultatul corect = 9. Dar merge doar pentru numere intregi, fara zecimale.
#result = float(num1) + float(num2)  # Aici am folosit functia `float` in loc de `int`, pentru a putea face operatia intre numere cu zecimale.
#print(result)

             #Mod libs game

#color = input("Enter a color")  # variabile si input
#plural_noun = input("Enter a Plural Noun")
#celebrity = input("Enter a celebrity")

#print("Roses are " + color)   ##Aici vrem ca userul sa introduca el ce cuvinte vrea. Este ca un joc de cuvinte aces Mad libs game
#print(plural_noun + " are blue")
#print("I love " + celebrity)

###Exercitiul meu 1
#name = input("Enter a name")
#skin_colour = input("Enter a skin colour")
#sex_type = input("Enter a sex type")

#print("He`s name is " + name)
#print("He`s skin colour is " + skin_colour)
#print("And he`s a " + sex_type)

###Exercitiul meu 2
#user = input("Enter a user")
#password = input("Enter a password")
#FA = input("Enter a FA")

#print("Username : " + user)
#print("Password : " + password)
#print("Your 2FA code is: " + FA)

             #Liste - O lista este o structura in Python ca sa stocam lista de informatii si valori si pe care sa le organizam si sa le tinem evidenta.
      # Aici folosim paranteze patrate si astfel Python va sti ca noi vrem sa creem o lista.
      # O variabila condtine doar o valoare, un string, un numar sau un Bulian value( True sau False), pe cand o `Lista` poate stoca mai multe valori intr-un singur obiect,
      # ca si cand o variabila ar putea contina mai multe valori, iar pentru a le diferentia, variabila devine lista.

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]  # friends acum este o lista, contine trei nume; folosim paranteze patrate si delimitam cu virgula.

print(friends)
print(friends[0])  # asa afisam parti din continut in functie de index(numar)
print(friends[1])
print(friends[2])
print(friends[-1])  # pentru a afisa de la coada catre cap, sau sfarsit catre inceput, putem incepe de la sfarsit cu -1, observam ca nu putem incepe cu zero, cum facem daca o luam in ordine crescatoare.
print(friends[-2])
print(friends[1:])  # daca punem doua puncte `:` in paranteza cu numarul de corespunde parantezei respective, ni se va afisa valoare corespunzatoare numarului dar si cele ce urmeaza.
print(friends[1:3])  # acum va afisa elementele 1 si 2 dar nu si pe cel corespunzator indexului 3.

    #Daca vrem sa modificam valorile in liste:

friends[1] = "Mike"  # Am redefinit numele de la Index 1
print(friends[1])  # Acum cand dau `run` imi va spune ca valoarea indexului 1 este Mike

        ##List functions

lucky_numbers = [4, 8, 15, 16, 23, 42]  #Prima lista

#lucky_numbers.sort()  #Aceasta functie scrie numerele in ordine ascendenta

#lucky_numbers.reverse() # Aceasta functie scrie elementele in ordine descrescatoare
### Observ un detaliu: dupa ce scriu functia, trebuie sa scriu print de acea lista dedesubt imediat, altfel nu efectueaza operatia.
print(lucky_numbers)
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#friends.extend(lucky_numbers)  ##extend este o functie prin care se adauga la lista friends, lista lucky_numbers ca si un appendice; se face efectiv un mix de liste.

#friends.append("Creed")  #Aceasta functie adauga inca un nume la lista friends.
#friends.insert(1, "Kelly")  # prin aceasta funtie am adaugat un element dupa indexul 1.
#friends.insert(2, "Kellu!)")
#friends.remove("Jim")  # Aceasta funtie ma ajuta sa elimin un element sau o valoare din lista mea.
#friends.clear()   # Cu aceasta functie elimin toate elementele din lista
#friends.pop()   # Aceasta functie imi elimina ultimul element din lista.

print(friends)
print(friends.index("Kevin"))  # Aceasta functie imi va da indexul(numarul/pozitia in lista) elementului care ma intereseaza.

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
#friends.sort()  # le pune in ordine ascendenta sau alfabetica

print(friends.count("Jim"))  # Imi arata de cate ori apare acel cuvant in lista ema, raspunsul corect este 2.

friends2 = friends.copy()  #Aici am atribuit continutul listei friends catre lista friends2. Cca se va folosy aceasta funtie mult.

print(friends2)




