print("Hello World!")
print("Hello again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

# A comment, this is so you cand read your program later.
# Anything after the # is ignored by python.

print("I could have code like this.")  # and the comment after is ignored

# you cand also use a comment to "disable" or comment out code:
# print("This won't run.")

print("This will run")

print("I will now count my chickens:")

print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")

my_name = 'Corina'
my_age = 31  # not a lie
my_height = 1.63  # m
my_weight = 53  # kg
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Light Brown'
print(f"Let's talk about {my_name}.")
print(f"She's {my_height} m tall.")
print(f"She's {my_weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"She's got {my_eyes} eyes and {my_hair} hair.")
print(f"Her teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}.")

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said:{x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end='')  # nothing happens
print(
    end7 + end8 + end9 + end10 + end11 + end12)  # cu end= '' se afiseaza intr-un cuvant, nu sare pe urmatorul rand, fara end='' afiseaza al doilea cuvand pe urm rand
                                                                #poti sa pui intre ghilimelele de la end="" orice semn de punctuatie. acesta se va pune la finalul stringului sau liniei scrise

# ex 8
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "own text here",
    "maybe a poem",
    "Or a song about fear"))

# ex9
# here's dome new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"  # functioneaza ca un ENTER

print("Here are days:", days)
print("Here are the months:", months)

print(""" 
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")  # cele trei ghilimele functioneaza ca un ENTER

# ex 10

tabby_cat = "\tI'm tabbed in."  # \t functioneaza ca un TABB
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."  # \\ functioneaza ca \

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# ex 11 - nu mai printeaza? se printeaza dupa ce raspunzi in terminal la intrebari. rolul "input"
# print("How old are you?", end=":")
# age = input()
# print("How tall are you?", end=":")
# height = input()
# print("How much do you weigh?", end=":")
# weigh = input()
# print(f" So, you're {age} old, {height} mm tall and {weigh} heavy.")

# print("Witch is you're favorite music?", end=",")
# music = input()
# print("Who is you're favorite Dj?", end=",")
# dj = input("Name: ") #in interiorul input pot sa adaug descriere, ce anume trebuie sa raspunda
# print(f" So, you're favorite music is {music}, and you're favorite Dj is {dj}.")

#ex.12
# age = input("How old are you?")
# height = input("Hor tall are you?")
# weigh = input("How much do you weigh")
#
# print(f"So, you are {age}, old, {height} mm tall and {weigh} heavy.")

# ex.13 - parameters,unpack, variables
# from sys import argv
#
# script, first, second, third = argv
#
# print("The script is called:", script)
# print("Your first variable is:", first)
# print("your second variable is:", second)
# print("Your third variable is:", third)
# #ex 14 - si ex 13 15 de reluat.

#ex de pe instagram
a = True
b = True
print(a==b)
print(a is b)

# #ex.30
# people = 20
# cars = 10
# trucks = 70
#
# if cars > people:
#     print ("We should take the cars.")
# elif cars < people:
#     print("We should not take the cars.")
# else:
#     print("We can't decide.")
#
# if trucks > cars:
#     print("That's too many trucks.")
# elif trucks < cars:
#     print("Maybe we could take the trucks.")
# else:
#     print("We still can't decide.")
# if people > trucks:
#     print("Alright, let't just take the trucks.")
# else:
#     print("Fine, let's stay home than.")
#
#
# #ex.31
# print(""" You enter a dark room with two doors.
# Do you go through door #1 or door #2?""")
#
# door = input(">")
# if door == "1":
#     print("There's a giant bear here eating a cheese cake.")
#     print("What do you do?")
#     print("1. Take the cake.")
#     print("2. Scream ar the bear.")
#
#     bear = input(">")
#
#     if bear == "1":
#         print("The bear eats your face off. Good job!")
#     elif bear == "2":
#         print("The bear eats your legs off. Good Job!")
#     else:
#         print(f"Well, doing {bear} is probably better.")
#         print("Bear runs away.")

#ex.32
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for cifre in the_count:
    print(f"This is count {cifre}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

#empty list, and use range function to do 0 to 5 counts
elements = []
for i in range(0, 6):
    print(f"lista este: {i} ")
    elements.append(i)
for i in elements:
    print(f"lista a fost alcatuita din:{i}")









