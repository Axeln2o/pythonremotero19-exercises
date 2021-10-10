str1 = "Welcome to Guru99 Python Tutorials"
print(f"The length of the string is: {len(str1)}")
s = "Whereof one cannot speak, thereof one must be silent."
print(s.upper())
print(s.lower())
str2 = 'Hi there'
print('The length of the string is:', len(str2))
print(str2.upper())
message = "python is fun"
print(f"The length of the message is: {len(message)}")
print(message.upper())
j = "This software is quite interesting. I would like to master it soon"
print(len(j))
j.upper()
print(j.upper())
x = 'my var'
y = 'some other var'
z = x
x = y
y = z
print(z + x)
x = 'Hello!'
z = 'How are you?'
temp = x
z = temp
print(x, z)
print(f'{x} {z}')


def my_function():
    my_variable = "s-a incalzit afara"
    print(my_variable)
    return my_variable


x = my_function()
print(x)


def my_function():
    my_var = "cmf"
    print(my_var)
    return my_var


x = my_function()
print(x)


def my_f():
    var = "I DON`T REALLY GET IT"
    return var


y = my_f()
print(y)


def my_rainbow():
    something = "fill"
    return something


xyz = my_rainbow()
print(xyz)

radius1 = 8
radius2 = 12
price1 = 2.5
price2 = 3.4
PI = 3.14


def circle_area_to_price(radius_x, price_x):

    area = PI * radius_x * radius_x
    return area/price_x


print(circle_area_to_price(radius1, price1))
print(circle_area_to_price(radius2, price2))

r1 = 8
r2 = 12
p1 = 2.5
p2 = 3.4
pi = 3.14
A1 = pi * r1**2
A2 = pi * r2**2
PA1 = A1 / p1
PA2 = A2 / p2
print(A1)
print(A2)
print(PA1)
print(PA2)


investment1 = 15000
investment2 = 250000
monthly_return1 = 500
monthly_return2 = 1500


def return_of_investment(investment, monthly_return):

    return investment // monthly_return


no_of_months1 = return_of_investment(investment1, monthly_return1)
no_of_months2 = return_of_investment(investment2, monthly_return2)


print(no_of_months1)
print(no_of_months2)

import requests

btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print(btc.json()['bpi']['USD']['rate'])
print(btc.json()['bpi']['GBP']['rate'])
print(btc.json()['bpi']['EUR']['rate'])

my_list = (11, 5, 17, 18, 23)
total = sum(my_list)
print("Sum of list: ", total)

import math

result1 = math.prod(my_list)
print("Multiply of list", result1)


list_a = [35, 7]
result = list_a[0] / list_a[1]
print(result)
print(int(result))

#shallow copy
nume1 = [0, 5, 'euro', 'dolari', 0.5]
nume2 = list(nume1)
nume1[0] = 'sambata'

print(nume1)
print(nume2)

import copy

nume11 = [0, 5, 'euro', 'dolari', 0.5, ['soare', 'copac']]
nume22 = list(nume11)
nume11[5][1] = 'zambet'

print(nume11)
print(nume22)

tabel = [1, 2, 'trei', 'patru', ['copac', 'frunza']]
tabel2 = copy.deepcopy(tabel)
tabel[4][1] = 'creanga'
print(tabel)
print(tabel2)


organigram = {
    "John": {
        "age": 35,
        "title": "CEO"
    },
    "Michael": {
        "age": 24,
        "title": "Admin"
    },
    "Iulica": {
        "age": 30,
        "title": "Director"
    }
}
print(organigram)


organigram["Adi"] = {
    "age": 32,
    "title": "Senior engineer"
}
print(organigram)
print(organigram["Adi"])
print(organigram.keys())
x = list(organigram.items())
print(x[0])

print(organigram.values())

del organigram["Adi"]
print(organigram)


# organigram.clear()
# print(organigram)

# organigram = {}
# print(organigram)

x = organigram.get("Iulica", "Adela")

print(x)
print(x["title"])
print(len(x["title"]))

print(x)

x["title"] = ["Manager", "Director"]

print(x)

x["title"].append("CTO")

print(x)


x = organigram


d = x["John"]
d["salary"] = 3000
d["currency"] = "EUR"

d = x["Michael"]
d["salary"] = 2500
d["currency"] = "EUR"
print(x)

d["currency"] = "GBP"
print(x)

x["John"]["currency"] = "EUR"
print(x)

print("Hello.")
user_name = input("Please say your name: ")
print(f"Hi, {user_name}!")

user_age = input("How old are you?")
print(f"I am, {user_age} old")
next_year_age = int(user_age) + 1
print(f"Next year I`ll be: {next_year_age}")


















































