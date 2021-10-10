import math
import pickle


def is_prime(nr):
    for x in range(2, int(math.sqrt(nr) + 1)):
        if nr % x == 0:
            return False
    return True


def first_primes(last, lista):
    count = 0
    nr = 2
    while count < last:
        if is_prime(nr):
            lista.append(nr)
            count += 1
        nr += 1


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

lista = []
first_primes(100, lista)

with open('file.pickle', 'rb') as file_in:
    lista_nr_prime = pickle.load(file_in)
    print(lista_nr_prime)

with open('file.pickle', 'wb') as file_out:
    pickle.dump(lista, file_out)


