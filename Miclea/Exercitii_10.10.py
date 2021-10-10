# pentru radicali se poate ridica la puterea 1/2
# ctrl+alt+l formateaza codul
# ctrl+alt++o sterge importurile care nu sunt necesare
# tuple_ = (1, 2, 3)  # imutable, indexable, duplicates allowed
# list_ = [1, 2, 3]  # mutable, indexable, duplicates allowed
# set_ = {1, 2, 3}  # mutable, unindexable, duplicates not allowed
# dict_ = {'a': 1, 'b': 2, 'c': 3}  # mutable, indexable, duplicates allowed on values, duplicates not allowed on keys
# a_tuple = tuple()
# a_list = list()
# a_dict = dict()
# a_set = set() #ca sa creezi un set gol
# # ctrl clik pe orice si te duce de unde ii
# print(list_[0:]) # from start to end
# print(list_[:len(list_)]) # from start to end
# print(list_[::2]) # from end to start, using step=-1

# list[start:stop:step]

# 1. Sa se scrie o functie pentru conversia gradelor celsius in fahrenheit
# 2. Sa se scrie o functie pentru conversia gradelor fahrenheit in celsius
# def celsius_fah(celsius):
#     fahren = celsius * 9 / 5 + 32
#     return fahren
#
#
# def fah_celsius(fahren):
#     celsius = (fahren - 32) / (9 / 5)
#     return celsius
#
#
# celsius = float(input('Gradele care le convertim: '))
#
# x_fahren = celsius_fah(celsius)
# print(x_fahren)
# x_celsius = fah_celsius(x_fahren)
# print(x_celsius)

# 3. Sa se scrie o functie care genereaza primele 100 numere prime
# def prim(n):
#     nrp = 0
#     for i in range(2, int(n ** 1 / 2) + 1):
#         if n % i == 0:
#             nrp += 1
#
#     if nrp == 0:
#         return True
#     else:
#         return False
#
#
# x = 0
# nr = 2
# while x < 5:
#     if prim(nr):
#         x += 1
#         print(nr)
#     nr += 1
# varianta a II-a
# def is_prime(num):
#     for index in range(2, int(math.sqrt(num)) + 1):
#         if num % index == 0:
#             return False
#     return True
#
#
# def generez(n):
#     contor = 0
#     pas = 0
#     while contor <= n:
#         if is_prime(pas):
#             print(pas)
#             contor += 1
#         pas += 1
#
#
# if __name__ == '__main__':
#     n = int(input("Dati n: "))
#     generez(n)
# Sa se scrie o functie care sa calculeze suma patratelor numerelor date
#
# def add_suma_patratelor(*args):
#     result = 0
#     for i in args:
#         result += i**2
#     return result
#     print(result)
#
#
#
#
# add_suma_patratelor(1, 2, 3)
# add_suma_patratelor(1, 2, 3, 4, 5, 6)

# Fiind dat un text in limba romana (cu diacritice), sa se scrie o functie care converteste literele# cu diacritice in litere fara diacritice, si returneaza textul modificat.

# def conv_diacrit(text):
#     print(text)
#     new_string = ""
#     for caracter in text:
#         if caracter == 'ă':
#             new_string += 'a'
#         elif caracter == 'ț':
#             new_string += 't'
#         elif caracter == 'ș':
#             new_string += 's'
#         elif caracter == 'â':
#             new_string += 'a'
#         elif caracter == 'î':
#             new_string += 'i'
#         else:
#             new_string += caracter
#     return new_string
#
#
# a = 'Bacău ( pronunție , supranumit și „orașul lui Bacovia”) este municipiul de reședință al județului cu același nume, Moldova, România.'

# print(conv_diacrit(a))
# varianta a II-a
# def conv_diac(txt):
#     diacritice = {'ă': 'a', 'ș': 's', 'ț': 't', 'î': 'i', 'â': 'a'}
#     for lit in txt:
#         if lit in diacritice:
#             txt = txt.replace(lit, diacritice[lit])
#     return txt
#
#
# text = 'George Bacovia (născut George Andone Vasiliu) n. 4/16 septembrie 1881, Bacău, România – d. 22 mai 1957,[2][3][4][5] București, România) '
#
# print(text)
# print(conv_diac(text))

# un OBIECT este instantierea unei clase

# CLASE

# class Animal:
#
#     def __init__(self, name, age, colour, species):
#         self.name = name  # set the default value for the name field of the Animal class object
#         self.age = age
#         self.colour = colour
#         self.species = species
#
#     def print_details(self):  # method for printing the state of an object
#         print(f"Name: {self.name}, age: {self.age}, colour: {self.colour}, species: {self.species}")
#
#
# my_dog = Animal("Bruna", 3, "maro", "caine")
# my_dog.print_details()
#
# my_cat = Animal("Tommy", 1, "gri", "pisoi")
# my_cat.print_details()

# CLasa protected
# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self._name = name
#         self._age = age
#
#
# my_dog = Animal()
# print(my_dog._name)  # It will give the value of the name field of the my_dog object

# Clasa privata
# class Animal:
#     def __init__(self, name="Rex", age=2):
#         self.__name = name
#         self.__age = age
#
#     def print_details(self):
#         print(f"name: {self.__name}, age: {self.__age}")
#
#
#
# my_dog = Animal()
# my_dog.print_details()  # Python will throw an error !!!


# class Animal:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property  # getter - get field value
#     def age(self):
#         return self.__age
#
#     @age.setter  # setter - sets a new field value
#     def age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be greater than 0.")
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if name == '':
#             print('Please input a name!')
#         else:
#             self.__name = name
#
#
# my_dog = Animal("Dog", 11)
# my_dog.age = 3  # Sets age - uses setter
# print(my_dog.age)  # Reads age - uses a getter
#
# my_dog.name = ''
# my_dog.name = 'Beni'
#
# print(my_dog.name)

# !!!toate metodele cu "__metoda__" se numesc magic methods

# class Human:
#     def __init__(self, name, height, weigth):
#         self.name = name
#         self.height = height
#         self.weigth = weigth
#
#
# class Programmer(Human):
#     def __init__(self, name, height, weigth, languages):
#         super().__init__(name, height, weigth)
#         self.languages ​​= languages
#
#
# bob = Programmer("Bob", 180, 100, ["Python", "Java"])
# print(bob.name)  # Access to the name field inherited from the Human class

# class Human:
#     def __str__(self):
#         return f"Name:{self.__name}, \nHeight: {self.__height}, \nWeigth: {self.__weigth} "
#
#     def __repr__(self):
#         return str(self)
#
#     def __init__(self, name, height, weigth):
#         self.__name = name
#         self.__height = height
#         self.__weigth = weigth
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         self.__height = height
#
#     @property
#     def weigth(self):
#         return self.__weigth
#
#     @weigth.setter
#     def weigth(self, weigth):
#         self.__weigth = weigth


#
# class Programmer(Human):
#     def __init__(self, name, height, weigth, languages):
#         super().__init__(name, height, weigth)
#         self.languages = languages
#
#
# om = Human("Corina", 162, 53)
# om1 = Human("Mihai", 172, 72)
# programator = Programmer("Ioana", 159, 55, ["Python", "Java"])
# print(om.height, om.weigth, om.name)
# print(om1)
#
# oameni = [om, om1]
# print(oameni)


# import pickle
#
# # writing to a file
# example_dict = {1: "6", 2: "2", 3: "f"}
# file_out = open("dict.pickle", "wb")
# pickle.dump(example_dict, file_out)
# file_out.close()
#
# # reading from a file
# file_in = open("dict.pickle", "rb")
# example_dict = pickle.load(file_in)
# file_in.close()
#
# # writing to a file using a context manager (to be studied at Python Intermediate)
# example_dict = {1: "6", 2: "2", 3: "f"}
# with open("dict.pickle", "wb") as file_out:
#     pickle.dump(example_dict, file_out)
#
# # reading from a file using a context manager (to be studied at Python Intermediate)
# with open("dict.pickle", "rb") as file_in:
#     example_dict = pickle.load(file_in)

import math
import os
import pickle


# writing to a file
# example_dict = {1: "6", 2: "2", 3: "f"}
# file_out = open("dict.pickle", "wb")
# pickle.dump(example_dict, file_out)
# file_out.close()
#
# # reading from a file
# file_in = open("dict.pickle", "rb")
# example_dict = pickle.load(file_in)
# file_in.close()
#
# # writing to a file using a context manager (to be studied at Python Intermediate)
# example_dict = {1: "6", 2: "2", 3: "f"}
# with open("dict.pickle", "wb") as file_out:
#     pickle.dump(example_dict, file_out)
#
# # reading from a file using a context manager (to be studied at Python Intermediate)
# with open("dict.pickle", "rb") as file_in:
#     example_dict = pickle.load(file_in)


def is_prime(num):
    for x in range(2, int(math.sqrt(num) + 1)):
        if num % x == 0:
            return False
    return True


def generez_primele_100_nr_prime(lista_nr_prime, initial_number):
    nr = initial_number
    pas = 0
    while pas < 100:
        if (is_prime(nr)):
            lista_nr_prime: list = lista_nr_prime
            lista_nr_prime.append(nr)
            pas += 1
        nr += 1

    return lista_nr_prime


if os.path.isfile('numere.pickle'):
    with open("numere.pickle", "rb") as file_in:  ##Citirea din fisier
        lista_nr_prime = pickle.load(file_in)
        print(lista_nr_prime)
else:
    lista_nr_prime = []
# Verificarea fisierului si generarea de numere prime
if len(lista_nr_prime) == 0:
    lista_nr_prime = generez_primele_100_nr_prime(lista_nr_prime, 2)
else:
    lista_nr_prime = generez_primele_100_nr_prime(lista_nr_prime, lista_nr_prime[-1])

# Scrierea "dump-ul" in fisierul nostru
with open("numere.pickle", "wb") as file_out:
    pickle.dump(lista_nr_prime, file_out)
