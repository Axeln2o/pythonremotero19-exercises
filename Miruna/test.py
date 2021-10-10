# 47. Write a Python program to insert an element before each element of a list.
# my_list = ['A', 'E', 'I', 'O', 'U']
# x = len(my_list)
# i = 0
# while i < 2*x:
#     my_list.insert(i, 5)
#     i = i+2
# print(my_list)

#46. Write a Python program to select the odd items of a list.
# my_list = [2,4,7,8,10,11,17,21]
# for x in my_list:
#     if x%2 == 0:
#         pass
#     else:
#         print(x)

#48. Write a Python program to print a nested lists (each list on a new line) using the print() function.
# l1 = [[1, 2, 3], ['a','b','c'], ['hello', 'one', 'two']]
# x = len(l1)
# for i in range(0, x):
#     print(l1[i])


# # 5. Write a Python program to count the number of strings where the string length is 2 or more and
# # the first and last character are same from a given list of strings.
# l2 = ['abc', 'xyz', 'aba', '1221']
# x = len(l2)
# result = []
# for i in range(0, x):
#     if l2[i][0] == l2[i][-1] and len(l2[i]) >= 2:
#         result.append(l2[i])
#     else:
#         pass
# print(len(result))

# 3. Write a Python program to sum all the values in a dictionary
# 	dic1={1:10, 2:20}
# 	Expected Result : 30
# dic1={1:10, 2:20, 3:30, 4:40, 5:50}
# value_list = dic1.values()
# x = sum(value_list)
# print(x)

#4. Write a Python program to get the maximum and minimum value in a dictionary
# dic1 = {1:10, 2:20, 3:30, 4:40, 5:50}
# k = sorted(dic1.values())
# min_max_list = []
# min_max_list.append(k[0])
# min_max_list.append(k[-1])
# print(min_max_list)

#2. Write a Python program to iterate over dictionaries using for loops
# dic1 = {"cats": 10, "dogs":20, "rabbits":5, "foxes":4, "horses":50}
# list1 = list(dic1.keys())
# for i in list1:
#     print(dic1[i])
#


# dic1 = {"cats": 10, "dogs":20, "rabbits":5, "foxes":4, "horses":50}
# print(dic1.get("cats"))

# 1. Write a Python script to concatenate following dictionaries to create a new one.
# 	Sample Dictionary :
# 	dic1={1:10, 2:20}
# 	dic2={3:30, 4:40}
# 	Expected Result : {1: 10, 2: 20, 3: 30, 4: 40}

from collections import counter
dic1={1:10, 2:20}
dic2={3:30, 4:40}
z = counter()


















