'''
Exceptions
'''

ok = False
a, b = None, None

while not ok:
    try:
        a = int(input('Introduceti a: '))
        ok = True
    except:
        print('a nu este un int, incearca din nou')

op = input('Introduceti operatorul: ')

ok = False

# while not ok:
#     try:
#         b = int(input('Introduceti b: '))
#         ok = True
#     except:
#         print('b nu este un int, incearca din nou')
b = input('Introduceti b: ')

result = None

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    # result = a / b  # programul se opreste la linia asta pentru ca nu este posibila impartirea la 0
    # print('Impartirea a esuat. Nu este posibila impartirea la 0')

    try:
        result = a / b
    except ZeroDivisionError:
        print('Impartirea a esuat. Nu este posibila impartirea la 0')
    except Exception as e:
        print(f'A aruncat o eroare dar nu este ZeroDivisionError')
        print(f'Exceptia este: {e}')

else:
    raise Exception(f'{op} nu este valid')

print(result)


