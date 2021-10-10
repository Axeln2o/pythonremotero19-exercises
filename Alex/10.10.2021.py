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
print(device_colour.isupper())  # Functie - afirmatie de verificare, imi va raspunde cu True sau False daca in functie de ceea ce eu am afirmat.
print(device_colour.islower())  # Functie - afirmatie de verificare, imi va raspunde cu True sau False daca in functie de ceea ce eu am afirmat.

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




