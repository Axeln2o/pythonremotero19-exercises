import math
import pickle


def is_prime(num):
    for index in range(2, int(math.sqrt(num)) + 1):
        if num % index == 0:
            return False
    return True


def generez_primele_100_nr_prime(lista_nr_prime):
    nr = 0
    pas = 0
    while pas < 100:
        if (is_prime(nr)):
            lista_nr_prime: list = lista_nr_prime
            lista_nr_prime.append(nr)
            pas += 1
        nr += 1

    return lista_nr_prime


lisa_nr_prime = []
lista_nr_prime = generez_primele_100_nr_prime

with open("numere.pickle", "rb") as file_in:  # citirea din fisier
    lista_nr_prime = pickle.load(file_in)
    print(lista_nr_prime)

# verificare fisier si generare nr prime
if lista_nr_prime is None:
    lista_nr_prime = generez_primele_100_nr_prime(lista_nr_prime, 2)
else:
    lista_nr_prime = generez_primele_100_nr_prime(lista_nr_prime, lista_nr_prime[-1])
