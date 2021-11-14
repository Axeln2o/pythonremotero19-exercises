

x = 10
y=10

if x+y > 19:
  raise Exception("Sorry, no sum of x and y is allowed above 19!")

x = 5
y=5

if x+y > 19:
  raise Exception("Sorry, no sum of x and y is allowed above 19!")

x="Asta nu e un int,e un string :o!"
if not type(x) is int:
  raise TypeError("Only integers are allowed")

l=lambda x,y:x+y
a=int(input("Give num"))
b=int(input("Give num"))
if l(a,b)>10:
  raise Exception("No sum above 10 is allowed!")
else:
  print("No error occured!")

l1=lambda x,y,z:x+y+z
a=int(input("Give triangle's length "))
b=int(input("Give triangle's length "))
c=int(input("Give triangle's length "))
if l1(a,b,c) >20:
  raise Exception("An error occured because total length of the traingle is above 20")
else:
  print(f"Triangle's total length is :{l1(a,b,c)}")