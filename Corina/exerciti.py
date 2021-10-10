# import requests
#
# btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
# print(btc.json())
# print(btc.json()['bpi'])
# print(btc.json()['bpi']['EUR']['description'])
# print(btc.json()['bpi']['EUR']['rate'])
#
# list_a = [35, 7]
# result = list_a[0] / list_a[1]
# print(result)
# print(int(result))
#
# #shallow copy
# nume1 = [0, 5, 'euro', 'dolari', 0.5]
# nume2 = list(nume1)
#
# nume1[0] = 'sambata'
#
# print(nume1)
# print(nume2)
#
# import copy
#
# nume11 = [0, 5, 'euro', 'dolari', 0.5, ['soare', 'copac']]
# nume22 = list(nume11)
#
# nume11[5][1] = 'zambet'
#
# print(nume11)
# print(nume22)
#
# tabel = [1, 2, 'trei', 'patru', ['copac', 'frunza']]
# tabel2 = copy.deepcopy(tabel)
# tabel[4][1] = 'creanga'
#
# print(tabel)
# print(tabel2)


# exercitii dictionar
import json

x = {
    "Corinne": {
        "age": 31,
        "title": "ceo"
    },
    "Jhon": {
        "age": 30,
        "title": "admin"
    }

}
# print(x)

# new_key= {"sallary": 3000}

# x["sallary"] = "3000 eur"
# print(x)

# d = x["Corinne"]
# d["salary"] = 3000
# d["currency"] = "EUR"
#
# d = x["Jhon"]
# d["salary"] = 2500
# d["currency"] = "EUR"
# print(x)
# d["currency"] = "GBP"
# print(x)
# x["Jhon"]["currency"] = "EUR"
# print(x)

# print(x["Corinne"])
# print(x.keys())

# a = list(x.items())
# print(a[0])
# print(x.values())
# x = {"age", "title", "sallary"}
# print(x)

# del (x["Corinne"])
# print(x)
# # x.clear()
# # print(x)
#
# # x = {}
# # print(x)
#
# c = x.get("Jhon", "Adela")
# print(c)
# print(type(c))
# print(c['age'])
# print(c['title'])
# t = len(c["title"])
# print(t)
#
#
# print(c)
# print(c["title"])
# c["title"] = ["admin", "sofer"]
# print(c)
#
# c["title"].append("cto")
# print(c)

# homework - 02.10.2021
# ex.1 - sum 2 dict.

from collections import Counter  # we have to import from collection the operation Counter, also in Collection there are -,&,|

x = {1: 20, 2: 20}
y = {3: 30, 4: 40}
z = dict(Counter(x) + Counter(y))
print(z)

x1 = {1: 20, 2: 20}
y1 = {3: 30, 4: 40}
x2 = {}
for i in (x1, y1): x2.update(i)

print(x2)

# ex.2 - to iterate over dict. using - for loops.

x1 = {"a": 2, "b": 4, "c": 6, "d": 8}
for x in x1:
    print(x)

# ex. 3/4 - to sum all the value from dict.

x2 = {1: 10, 2: 20}
z2 = sum(x2.values())
z3 = min(x2.values())
z4 = max(x2.values())
print(z2)
print(z3)
print(z4)

# ex. 5 - print dict line by line
import _json

categorii = {"Tip Deseu": {"Deseuri periculoase": "ulei uzat", "cod deseu": "13 06 06"},
             "Tip Deseu1": {"Deseuri nepericuloase": "Hartie/Carton", "cod deseu": "15 01 01"}}
print(json.dumps(categorii, indent=4))

# ex.46 - select odd items from list

multime_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in multime_lista:
    if num % 2 != 0:
        print(num, end=";")

# ex. 47 - insert element before each element of a list
waste_list = ["paper", "iron", "plastic", "wood"]
print(waste_list)
waste_list = [v for elt in waste_list for v in ('of', elt)]
print(waste_list)

# tips of the day - 10.08.2021 - just for string, in list doesn't work.
s = "a, b, c"
print(s.split(","))

# 48 - nested list

pranz = [["supa de pui, ciorba de vacuta"], ["cartofi cu snitel, paste carbonara"], ["chessecake, papanasi"]]
for xs in pranz:
    print("".join(map(str, xs)))

# 5 count num of string ???? nu inteleg exercitiul

documente = "15, act identitate, contract inchiriere, cod CAEN, CUI: 235720, 15"


def match_words(words):
    ctr = 0

    for documente in words:
        if len(documente) > 1 and documente[0] == documente[-1]:
            ctr += 1
            return ctr


print(match_words("15, act identitate, contract inchiriere, cod CAEN, CUI: 235720, 15"))
