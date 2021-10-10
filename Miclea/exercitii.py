# encode si decode folosesti la utf-8 pentru a comunica serverul cu browser

# hello = "hello world"
# print(hello[::-1]) #printeaza invers

# import requests
#
#
# btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
# print(btc.json())
# print(btc.json()['bpi']['EUR']['symbol'])
# print(btc.json()['bpi']['GBP']['description'])

# Shallow copy la liste la un nivel superficial
# a = [1, "sds", 4]
# list_2 = list(a)  daca modificam a, se modifica si list 2
# Deepcopy cand nu mai folosit list(),
# import copy
# x = [1, 3, 5] daca modificam x, nu se modifica y
# y = copy.deepcopy(x)

# 1. Write a Python program to sum all the items in a list.

# import math
#
#
# my_list = [1, 3, 5, 7]
#
# print(sum(my_list))
#
# # 2. Write a Python program to multiply all the items in a list.
#
# print(math.prod(my_list))
#
# print(max(my_list))
#
# print(min(my_list))

# Dictionar  Timp constant (la dictionar mergem instant)
# Lista  Timp liniar (cand parcurgem o lista)
angajati = {
    'Jiji': {
        'varsta': 34,
        'salar': 4500,
        'pozitie': 'Director'
    },
    'Duru': {
        'varsta': 23,
        'salar': 2500,
        'pozitia': 'sef de raion:))'
    },
    'Aurica fara frica': {
        'varsta': 33,
        'salar': 3200,
        'pozitia': 'bodyguard'

    }

}
print(angajati)

angajati['Patrunjel'] = {
        'varsta': 28,
        'salar': 2000,
        'pozitia': 'scoala vietii'
}

print(angajati)

print(angajati['Patrunjel'])

print(angajati.keys())

x = list(angajati.items())  # am transformat itemu in lista ca sa putem sa le indexam


print(x[0])


# overflow ii foarte buni pentru erori

print(angajati.values())

del angajati['Duru']

print(angajati)

# angajati.clear()

# print(angajati)

#  garbage colector arunca la cos obiectele care nu au referinta in cod

# print(angajati.get('Mihai', '') == 0)
#
# y = len(angajati.get('Mihai', ''))
#
# print(y == 0)
#
#
# print(y)
#
# z = angajati.get('Jiji')
#
# print(z)

# z['pozitie'] = ['Manager', 'ospatar']
#
# print(z)
#
# z['pozitie'].append('CFO')
#
# print(z)
#
# a = angajati['Aurica fara frica']
# a['currency'] = 'EUR'
#
# print(a)
#
# a['varsta'] = [33, 'ani']
#
#
# print(a)


# print('Hello')
#
# user_name = input('Print you name: ')
# user_musiq_type =  input('What musiq u like: ')
# user_age = int(input('Your age: '))
# user_age += 1
# print(f'Welcome to our world, {user_name}!, we all listen {user_musiq_type} when we are drunk!')
# print(f' Next year you will be: {user_age}')


x = 0
y = 3
# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == 3:
#     print(f'{x} is equal {y}')
# else:
#     print(f'{x} is less than {y}')

#
# while x < y:
#     print(x)
#     x = x + 1
# print(x) # dupa ce intra in while ajunge la valoare 3 si ramane asa

# n = 0
# while n < 5:
#     n += 1
#     if n == 4:
#         break
#     if n == 1:
#         continue
#     print(n)

animals = [ "dog", "cat", "fish"]
i = 0

for x in animals:
    print(i)
    i = i + 1
    print(i)

    if i == 1:
        pass