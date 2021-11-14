''' Exceptions'''

ok = False
a, b = None, None

while not ok:
    try:
         a = int(input('Introduceti a: '))  #adica aici trebuie sa pun eu valori de la tastatura dupa ce dau run
         ok = True
    except:
        print('a nu este un int, incearca din nou')


op = input('Introduceti operatorul: ')


ok = False

while not ok:

    try:
        b = int(input('Introduceti b: '))
        ok = True
    except:
        print('b nu este un int, incearca din nou')


result = None

if op == '+':
    result = a + b
if op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    try:
        result = a / b   # La diviziunea cu 0 se opreste la linia asta
    except:
        print('Impartirea a esuat')
else:
    raise Exception(f'{op} nu este valid')  # creem intentionat o exceptie

print(result)
