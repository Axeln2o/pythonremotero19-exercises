# Sa se scrie o functie care genereaza primele 100 numere prime
import math
def is_prime(num):
    for index in range(2, int(math.sqrt(num)) + 1):
        if num % index == 0:
            return False
    return True
#
#
# def generez(n):
# #     contor = 0
# #     pas = 0
# #     while contor <= n:
# #         if is_prime(pas):
# #             print(pas)
# #             contor += 1
# #         pas += 1
# #
# #
# # if __name__ == '__main__':
# #     n = int(input("Dati n: "))
# #     generez(n)
# #ex.2
#
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