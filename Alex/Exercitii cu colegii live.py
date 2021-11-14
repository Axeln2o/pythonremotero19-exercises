#Sintaxa = regula de scriere, ca asezare in pagina dar si ca legatura intre operatii.

 #1: creez antetul functiei - ala cu def, se scriu si parametri intre paranteze
 #2: creez corpul functiei - cel sub antet
 #3: imi initializez toate variabilele de care cred ca am nevoie
 #4: citesc de la tastatura textul initial
 #5: apelez functia

#def citire(text):
   # print(text)

#vremea = input("starea vremii: ")

#citire(vremea)

def avg(num1, num2, num3, count):  # media aritmetica
    s = float(num1 + num2 + num3)
    return float(s/count)

print(avg(1, 3, 5, 3))

for x in range(0,5):
    num1 = input("num1")
    num2 = input("num2")
    num3 = input("num3")
    count = input("dati nr de nr")
    print(str(avg(num1 + num2 + num3 +count)))


