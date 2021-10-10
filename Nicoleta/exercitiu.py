# Sa se scrie o functie pentru conversia gradelor celsius in fahrenheit

# def celsius_fahren(celsius):
#     fahren = celsius * 9 / 5 + 32
#     return fahren
#
#
# def fahren_celsius(fahren):
#     celsius = (fahren - 32) / (9 / 5)
#     return celsius
#
#
# celsius = float(input("Ce grade vrei sa convertesti : "))
# x_fahren = celsius_fahren(celsius)
# print(x_fahren)
# x_celsius = fahren_celsius(x_fahren)
# print(x_celsius)


# Sa se scrie o functie care genereaza primele 100 numere prime
import math


def is_prime(num):
    for index in range(2, int(math.sqrt(num)) + 1):
        if num % index == 0:
            return False
    return True


def generez(n):
    contor = 0
    pas = 0
    while contor <= n:
        if is_prime(pas):
            print(pas)
            contor += 1
        pas = +1


if __name__ == '__main__':
    n = int(input("Dati n:"))
    generez(n)
