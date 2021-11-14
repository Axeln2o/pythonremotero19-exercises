#List Comprehension este o modalitate prin care poti genera o lista dandu-io  regula
#Modelul clasic este:
l = [4, 5, 10, 20]
my_list = []
for i in l:
    if i<15:
        my_list.append(i)
print(my_list)

#Modelul cu list comprehension:
l = [4, 5, 10, 20]
my_list = [i for i in l if i<15]
print(my_list)

#Create an identical list from the first list using list comprehension.

lst1=[1,2,3,4,5]


lst2= [i for i in lst1]

print(lst2)

#Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.

rng= range(1200,2000,130)

lst=[i for i in rng]

print(lst)

#Use list comprehension to contruct a new list but add 6 to each item.

lst1=[44,54,64,74,104]

lst2=[i+6 for i in lst1]


print(lst2)

#Using list comprehension, construct a list from the squares of each element in the list.

lst1=[2, 4, 6, 8, 10, 12, 14]


lst2=[i**2 for i in lst1]


print(lst2)

#Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.

lst1=[2, 4, 6, 8, 10, 12, 14]


lst2=[i*i for i in lst1 if i*i > 50]


print(lst2)

#Given dictionary is consisted of vehicles and their weights in kilograms. Contruct a list of the names of vehicles with weight below 5000 kilograms. In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}


lst=[key.upper() for key in dict if dict[key] < 5000 ]

print(lst)
