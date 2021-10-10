# import copy
# import math
# from collections import Counter
# from inspect import Traceback
#
# def medie_aritmetica(a, b):
#     return (a + b) / 2
#
#
# print(medie_aritmetica(10, 100))
# medie_aritmetica(10, 100)
#
#
# # this function calculate the average of two numbers
#
# def print_hi(name):
#     """
#
#     :rtype: object
#     """
#     print(f"Hi, {name}")
#     if __name__ != "__main__":
#         pass
#     else:
#         print_hi("Diana!")
#
#
# # Write a function that will determine the division between 2 numbers
#
# def medie(a, b):
#     return a / b
#
#
# print(medie(6, 3))
#
#
# # Write a functionat that should compute the average of 2 numbers;
# # Hints:  compute_average(2,6)  // should output (2+6)/2 -> 4
# def compute_average(a, b):
#     return (a + b) / 2
#
#
# print(compute_average(3, 6))
#
# # Create function that will receive a string and will return upper case string
# my_string = "diana"
# string1 = my_string.upper()
# print(string1)
#
#
# def string_convertor(string1):
#     return string1.upper()
#
#
# print(string_convertor("mihai"))
#
# # Create function that receives 1 string and returns the length
# my_string = "abcde"
# print(len(my_string))
#
#
# def lungime_sir(string1):
#     return (len(string1))
#
#
# print(lungime_sir("Diana si Mihai"))
#
# # Swap 2 variables that are pointing to strings and concatenate them
# a = "Diana"
# b = "Mihai and "
# d = a + b
# print(d)
# a, b = b, a
# c = a + b
# print(c)
#
#
# # Write a program (or function) that will compare the area/price ratio between two pizzas.
# # In order to calculate the area of a circle P at a given radius r - use this formula - Formula.
# # Find a restaurant in your area, enter the appropriate data and answer the question asked in the recommendation.
#
# # def best_pizza(r1, price1, r2, price2):
# #     if (r1 ** 2 / price1) * (price2 / r2 ** 2) > 1:
# #         print("Choose this Pizza1!!")
# #     else:
# #         print("Pizza1 is not worth it!!")
# #
# #
# # print(best_pizza(2, 15, 4, 12))
#
# # Write a program that checks if a given number is preceded by a prime number
#
# import math
#
#
# def isPrime(n):
#     if (n <= 1):
#         return False
#     else:
#         for x in range(2, int(math.sqrt(n) + 1)):
#             if (n % x) == 0:
#                 return False
#             else:
#                 return True
#
#
# print(isPrime(17))
#
#
# # Write a function (or program) that will calculate the zeros of the given square function.
# # For this purpose, you can use the formulas presented here: ax**2+bx+c = 0
# # x1= [-b+/-sgrt(b**2-4ac)]/2a
#
#
# # Write a function (or program) that will correctly display the sentence "Alice has x cats"
# # depending on the number of cats.
#
# def Alice_catmom(a):
#     if a == 1:
#         print("Alice has {} cat!".format(a))
#     else:
#         print("Alice has {} cats".format(a))
#
#
# print(Alice_catmom(1))
#
# c = Counter({'red': 4, 'blue': 2})
# print(c)
# c
#
# name = "John"
# greeting = "Hello, " + name
# print(greeting)
#
# message = "Hi"
# print(message * 2)
#
# num = 3
# num = num + 4
# print(num)
# num += 5
# print(num)
# num -= 2
# print(num)
# num /= 2
# print(num)
# num **= 3
# print(num)
# num = num // 2
# print(num)
# john_1 = "John"
# john_2 = "John"
# print(john_1 == john_2)
# print(-32 >= -33)
# print(123 <= 123)
#
# title = "General"
# name = "Kenobi"
# print("Hello there {} {}!".format(title, name))
#
# title = "General"
# name = "Kenobi"
# print("Hello there, {0} {1}".format(title, name))
#
# header1 = "Name"
# header2 = "Age"
# name = "John"
# age = 22
#
# print(f"| {header1} | {header2} |")
# print("-" * 27)
# print(f"| {name} | {age} |")
#
# import math
#
#
# def find_roots(a, b, c):
#     if a == 0:
#         return False
#     else:
#         x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
#         y = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
#         my_list = [x, y]
#         return my_list
#
#
# print(find_roots(1, -2, 1))
#
# # import requests
# #
# # btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
# # print(btc)
# # print(btc.json()['bpi']['USD']['rate'])
# # print(btc.json()['bpi']['EUR']['description']['rate'])
# #
# # x=[[1,2,3],[4,5,6]]
# # x
# #
# #
# # my_list = ['a','b','c','d']
# # print(my_list)
#
#
#
# # list.pop()
# # print(list)
#
# # abc = [0, 5, "jim", "sam",0.5]
# # efg = list(abc)
# # abc[0] = "ana"
# # print(abc)
# # print(efg)
# #SHADOW LIST!!! EX1
# # list1 = [1,2,3,4,5]
# # list2 = list(list1)
# # list1[0] = "A"
# # print(list1)
# # print(list2)
#
# #SHADOW LIST!!! EX2
# # list1 = [1,2,['a','b','c']]
# # list2 = list(list1)
# # list1[2][0] = 'X'
# # print(list1)
# # print(list2)
#
# # list1 = [1,2,['a','b','c']]
# # list2 = list1
# # list1[2][0] = 'X'
# # print(list1)
# # print(list2)
#
#
# #a kind of DEEP COPY!!
# # list1 = [1,2,3,4,5]
# # list2 = list1
# # list1[0] = "A"
# # print(list1)
# # print(list2)
#
# #real DEEP COPY
# # list1 = [1,2,3,4,5]
# # list2 = copy.deepcopy(list1)
# # list1[0] = "A"
# # print(list1)
# # print(list2)
#
# # list1 = [1,2,['a','b','c']]
# # list2 = copy.deepcopy(list1)
# # list1[2][0] = "X"
# # print(list1)
# # print(list2)
# #
# # catalog = {"John":{"prezenta":0, "nota":10}, "Ana":{"prezenta":0, "nota":10}}
# # catalog
#
# #Definirea unui dictionar
# #
# # org = {
# #     "John": {
# #         "Age": 45,
# #         "Title": "CEO"
# #     },
# #     "Mike": {
# #         "Age": 39,
# #         "Title": "Admin"
# #     },
# #     "Iulica": {
# #         "Age": 51,
# #         "Title": "Director"
# #     }
# # }
# # print(org)
# # org ["Ann"] = {
# #     "Age": 21,
# #     "Title": "PM"
# # }
# # print(org["Ann"])
# # print(org["Mike"])
# #
# # print(org.keys())
# # print(org.items())
# #
# # x = list(org.items())
# # print(x[0])
# # print(org.values())
# #
# # del org["Ann"]
# # print(org)
# #
# # # org.clear()
# # print(org)
#
# # org = {}
# # print(org)
#
# # print(len(org.get("Mihai","Adel")) == 4)
# # print(len(org.get("Adi","Adel")) == 4)
# # print(len(org.get("Iulica","Adel")) == 4)
#
# # x = org.get("Iulica","Adel")
# # print(x)
# # x["Title"] = ["Manager", "Director"]
# # print(x)
# # x["Title"].append("CTO")
# # print(x)
# # print(org)
#
#
# #
# #
# # org = {
# #     "John": {
# #         "Age": 45,
# #         "Title": "CEO"
# #     },
# #     "Mike": {
# #         "Age": 39,
# #         "Title": "Admin"
# #     },
# #     "Iulica": {
# #         "Age": 51,
# #         "Title": "Director"
# #     }
# # }
# # print(org)
# # org ["Ann"] = {
# #     "Age": 21,
# #     "Title": "PM"
# # }
# #
# # print(org["Mike"])
# # d = org["Mike"]
# # d["salary"] = 3000
# # d["currency"] = "EUR"
# # print(org)
# #
# # d = org["John"]
# # d["salary"] = 3500
# # d["currency"] = "EUR"
# # print(org)
# #
# # org["John"]["salary"] = 4500
# # print(org)
# # org["John"]["currency"] = "GBP"
# # print(org)
# #
# # print("Hello!")
# # user_name = input("Pls say your name:")
# # print(f"Hi, {user_name}")
# # user_age = input("Pls say your age:")
# # print(f"Hi, I'm {user_age}")
#
# # x = 0
# # y = 3
# # if x > y:
# #     print(f"{x} is greater than {y}")
# # else:
# #     print(f"{x} is less than {y}")
# #
#
# x = 0
# y = 3
# # if x > y:
# #     print(f"{x} is greater than {y}")
# # elif x == y:
# #     print(f"{x} is equal to {y}")
# # else:
# #     print(f"{x} is less than {y}")
# #
#
# #
# # while x < y:
# #     print(x) # prima val pe care o afiseaza x este 0
# #     x = x + 1 # devine 1
# # print("Finish")
# #
# # # x = print # x a luat comportamentul lui "print"!! Python este extrem de flexibil
# # x("Finis")
#
# # # Cum se iese din bucla WHILE pe parcurs, nu la capat total!!
# # # exista 2 cuv rezervate: break - iese complet din WHILE, continue -
# #
# # n = 0
# while n < 5:
#     n += 1
#     if n == 4:
#         print("n is 4")
#     elif n == 1:
#         print("n is 1")
#         break
#
# animals = ["Dog","Cat","Fish"]
# i = 0
# for x in animals:
#     print(animals[i])
#     i = i+1
#     if i == 1:
#         # pass # cand nu vrei s afaci NIMIC!!
#         # break
#     # print(x)
# # print(animals[i])

# 46. Write a Python program to select the odd items of a list.
# my_list = [2, 4, 7, 8, 10, 11, 17, 21]
# for x in my_list:
#     if x % 2 == 0:
#         pass
#     else:
#         print(my_list)
#
#
# my_list = [2,4,7,8,10,11,17,21]
# for x in my_list:
#     if x%2 == 0:
#         pass
#     else:
#         print(x)

my_list = ['A', 'E', 'I', 'O', 'U']
x = len(my_list)
i = 0
while i in range(0, x-1):
    if i == 0:
        my_list.insert(i, 5)
    else:
        i = i+2
        my_list.insert(i, 5)
print(my_list)


























