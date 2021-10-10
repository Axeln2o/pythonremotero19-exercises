# my_list = [1, 3, 5, 7]
# print(sum(my_list))
#
# import math
#
# result1 = math.prod(my_list)
# print("Multiply:", result1)
#
# list= [35, 7]
# result = list[0] / list[1]
# print(result)

import random

x = 10
y = 8

if x >y:
    print(f"{x} is is greater than {y}")

elif x == 3:
    print(f"{x} is equal {y}")

elif x == y:
    print(f"{x} is equal with {y}")

else:
    print(f"{x} is less than {y}")

anotimpuri = ["primvara", "vara", "toamna", "iarna", "anotimpul special"]

print(anotimpuri)

#for anotimp in anotimpuri:
#    print(anotimp)


print('-------------------------------------')
cnt = 0
print("Cnt este " + str(cnt))
while cnt != len(anotimpuri):
    print(anotimpuri[cnt])
    cnt += 1

print ("------------------------------------------")

while anotimpuri:
    #element = len(anotimpuri) -1
    element = 0

    print(anotimpuri[element])
    anotimpuri.__delitem__(element)

print ("------------------------------------------")

anotimpuri = ["primvara", "vara", "toamna", "iarna", "anotimpul special"]

while anotimpuri:
    element = random.randrange(0, len(anotimpuri))

    print(anotimpuri[element])
    anotimpuri.__delitem__(element)


tuple = (1, 2, 3) #imutabil, indexable, duplicates allowd
list = [1, 2, 3] #mutable, indexable, duplicate allowed
set = {1, 2, 3} #mutable, unindexable, duplicate not allowed
dict = {'a': 1, 'b': 2, 'c': 3}

















