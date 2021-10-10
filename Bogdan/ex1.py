# 1. Scrieti 2 functii pentru conversia temperaturilor kelvin <-> celsius
def conv_kelvin_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


def conv_celsius_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


metoda = input("""
In ce vrei sa convertesti?
Kelvin sau Celsius
""")
if metoda == 'k' or metoda == 'K' or metoda == 'kelvin' or metoda == 'Kelvin':
    temp = int(input("Care este temperatura pe care vrei sa o convertesti?:\n"))
    print(conv_celsius_kelvin(temp),'K')
else:
    if metoda == 'c' or metoda == 'C' or metoda == 'celsius' or metoda == 'Celsius':
        temp = int(input("Care este temperatura pe care vrei sa o convertesti?:\n"))
        print(conv_kelvin_celsius(temp),'C')
