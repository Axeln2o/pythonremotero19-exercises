#Tuples - a tuple is a container where you can store different values, very similar to a list, but there are a few key differences.
#Tuple este `immutable` - nu poate fi schimbat sau modificat, nu poti adauga elemente, nu poti sterge elemente
#Dupa exercitiul de mai jos, inteleg ce facea Adi in curs, atunci cand selecta numere din matrice prin aceste paranteze patrate
coordinates = (4, 5)
#daca vrem sa scriem coordinates[1] = 10, adica sa scimbam 5-ul cu 10, ne va da eroare si va spune ca tuple este immutable
print(coordinates[0])
print(coordinates[1])
#putem creea o lista de tuples:
coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates[1])  # aici mi-a printat perechea

   #Functii - a collection of code which performs a specific task; ne ajuta sa ne organizam mai bine codul

#Vrem sa creem o functie care spune `Hi` unui user
#prin `def` se incepe intotdeauna o functie; `say_hi` este numele functiei; tot timpul se pun dupa doua paranteze si doua puncte
# pe randul de sub `def` se va incepe automat cu alineat, se spune indented sau in romana probabil indentat.
def say_hi():
    print("Hello User")
# dupa ce am scris cele de mai sus, acum trebuie sa `call this function`

say_hi()     #am facut `call the function` prin a scrie numele ei si a pune cele doua paranteze

# un parametru este o bucata de informatie pe care io dam unei functii

def say_hi(name):                #Vrem sa spunem Hy to a person, si ii dam un nume, deci daca `name` devine corpul funtiei dintre paranteze, atunci cand dam print de `name`, imi va afisa orice pun eu in paranteze.
                                # Imi va afisa ori de cate ori scriu numele funtiei
    print("Hello" + name)
say_hi(" Mike")
say_hi(" Steve")
say_hi(" George")

def say_hi(name, age):
    print("Hello" + name + " you are " + age)

say_hi(" Mike", "35")
say_hi(" Steve", "40")
say_hi(" George", "15")

def say_hi(name, age):
    print("Hello" + name + " you are " + str(age))   # daca vreau sa pun mai jos varsta fara ghilimele, modific aici `+ age` cu `+ str(age)

say_hi(" Mike", 35)   # dupa cum se observa, comparativ cu mai sus, aici am scos ghilimelele.
say_hi(" Steve", 40)

    #`Return` statement  - print `return` functia ne poate oferi o informatie de care avem nevoie dintr`o functie

     #Exercitiu de ridicare la puterea a treia
def cube(num):    #Exemplul 1: cand iam dat `run`, mi-a scris `None`, adica nu mi-a returnat nici un rezultat.
    num*num*num  # s-a inmultit numarul de 3 ori, gen la a treia

print(cube(3))

def cube(num):    # Exemplul 2: cand i-am dat `run`, mi-a returnal `27`, adica 3 la a treia
    return num * num * num
print(cube(3))
print(cube(4))

def cube(num):    # Exemplul 3: putem folosi si o variabila
    return num * num * num
result = cube(4)
print(cube(4))

def sum(num):     #Exemplul meu
    return num+num+num

print(sum(2))

    #`If statements`  - pot sa execut coduri si la le pun conditia daca sunt adevarate sau nu
       # Ele trebuie sa raspunda la `input` - ul pe care il introduc eu

is_male = True  #True este un bulion - remember

if is_male:
    print("You are a male")   # pentru ca afirmatia este adevarata, python va printa propozitia dupa ce ii dau `run`
else:   # conditia - otherwise
    print("You are not a male")  # nu va printa nimic pentru ca nu este adevarat

is_male = False

if is_male:
    print("You are a male")  #Pentru ca am folosit `False`, programul nu va mai printa nimic aici
else:
    print("You are not a male") # Dar va printa aici

is_male = True  #True este un bulion - remember
is_tall = True

if is_male or is_tall:   # aici va printa daca una din conditii este adevarata
    print("You are a male or tall or both")
else:
    print("You neither male or tall")

is_male = False  # Facem experiment si cu False
is_tall = False   # Aici ne putem juca cu bulionul sa vedem cum se schimba rezultatele

if is_male and is_tall:   # aici va printa doar daca ambele conditii sunt adevarate
    print("You are a tall or both")
elif is_male and not(is_tall):   #`elif` vine de la `else` si `if`
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a short male")
else:
    print("You are either not male or not tall or both")

  #If statements & Comparisons

#def max_num(num1, num2, num3):
   # if num1 >= num2 and num1 >= num3:   # `>+` - comparison operator `!=`- asta inseamna `not equal`
      #  return num1
    #elif num2 >= num1 and num2 >= num3:
       # return num2
    #else:
        #return num3

#print(max_num(3, 4, 5))

  #Building a better calculator - deci userul va introduce un nr., apoi un semn de operatie apoi alt numar si se va face calculul

#num1 = float(input("Enter first number: ")) # nu prea am inteles aici de ce a folosit`FLOAT`; spune ca pentru a evita ca Python sa printeze interiorul parantezelor ca pe un string si sa fie sigur ca printeaza un numar.
#op = input("Enter operator: ")  # `operator` este semnul + - / *
#num2 = float(input("Enter second number"))

#if op == "+":
    #print(num1 + num2)
#elif op == "-":
   # print(num1 - num2)
#elif op == "/":
   # print(num1 / num2)
#elif op == "*":
   # print(num1 * num2)
#else:
    #print("Invalid operator")

  # Dictionaries - ne permite sa creem Key value pairs

monthConversions = {   # Aici `Jan` poate fi considerat cuvatul si `Januari` este definitia cuvatului respectiv, la fe lca intr-un dictionar explicativ.
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])

print(monthConversions.get("Dec"))

print(monthConversions.get("Luv"))

   #While loop   - ne permite sa executam o parte de cod de mai multe ori, atata timp cat se respecta `conditia` : 1<10

#i = 1
#while i < 10:
    #print(i)
    #i += 1

   # print("Done with loop")

a = 5  # exemplul meu
while a <= 5:
    print(a)
    a += 1



