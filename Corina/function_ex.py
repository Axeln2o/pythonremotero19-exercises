# scrieti o functie care sa calculeze suma patratelor numerelor date
def add_squares(*args):
    print(args)
    result = 0
    for arg in args:
        result += arg ** 2
    return result

print(add_squares(1, 2, 3))
print(add_squares(2,2,2))

def multiply_num(*args):
    result = 1
    for arg in args:
        result = result+1 * args
        return result

print(multiply_num(2,5))
