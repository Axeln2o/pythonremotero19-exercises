#"Fisierul" cu convertor.py

def celsius_fahren(celsius):
    fahren = celsius * 9 / 5 + 32
    return fahren


def fahren_celsius(fahren):
    celsius = (fahren - 32) * 5 / 9
    return celsius


if __name__ == '__main__':
    n = int(input("Dati gradele "))
    print(fahren_celsius(n))