def celsius_fahren(celsius):
    fahren = celsius * 9 / 5 + 32
    return fahren


def fahren_celsius(fahren):
    celsius = (fahren - 32) /( 9 / 5)
    return celsius


celsius = float(input(f'Ce vrei sa convertesti: '))
x_fahren = celsius_fahren(celsius)
print(x_fahren)
x_celsius = fahren_celsius(x_fahren)
print(x_celsius)
