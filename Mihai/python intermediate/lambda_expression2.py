items = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, items))  # [1, 4, 9, 16, 25]
odds = list(filter(lambda x: x % 2 ==1, items))  # [1, 3, 5]
print(odds)

from functools import reduce
items_sum = reduce(lambda x, y: x + y, items)  # 15
print(items_sum)


lista=[999,10,232,11,2323]
lista=reversed(lista)
print(lista)
