print ("hello ")

print(f' {4 / 2} is the result of 4 divided to 2')

from statistics import mean

number_list = 2, 4, 6, 8, 100
avg = mean(number_list)
print(f'The average of 2,4,6,8 and 100 is: {avg}')

my_variable = 'This is life'
len(my_variable)
print(f'the sum of the characters in this affirmations is: {len(my_variable)}')

my_variable = my_variable.upper()
print(f'{my_variable} is to be viewed with an optimistic mindset')

x = 'Hello!'
z = 'How are you?'
temp = x
x = z
z = temp
print(x, z)
print(f'{x} {z}')


def my_function():
    my_variable1 = 'Nu poti sa vrei ce vrei sa poti'
    return my_variable1


x = my_function()
print(x)

# Exercitiu Pizza
pizza_1 = 3.14 * 7 ** 2
print(pizza_1)

pizza_2 = 3.14 * 5.2 ** 2
print(pizza_2)

price_on_slice1 = pizza_1 / 31
price_on_slice2 = pizza_2 / 27

print(f'pretul pentru pizza 1 {price_on_slice1}')
print(f'pretul pentru pizza 2 {price_on_slice2}')

radius1 = 7
radius2 = 5.2
price1 = 31
price2 = 27


def circle_area_to_price1(r, p):
    PI = 3.14
    area = PI * r ** 2
    return area / p


print(circle_area_to_price1(radius1, price1))
print(circle_area_to_price1(radius2, price2))
