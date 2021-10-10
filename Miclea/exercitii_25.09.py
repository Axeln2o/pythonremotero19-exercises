# type() verifica tipul obiectului
# // iti da intregul din impartire
# ord()codul ASCII
# dir() iti arata toate functile pe care le poate face ... gen dir(int)

my_string = " Nu am idee ce sa scriu aici"
# print(my_string)
print(my_string.upper())
print(len(my_string))

new_string = "Nu glumesc"

print(f"{my_string} {new_string}")


def my_function():  # creem o functie
    first_var = "Ramanem fara idei"  # declaram o variabila
    # print(first_var)
    return first_var  # fara return nu stie ce sa returneze


# print(my_function()) ar fii prima varianta

# sau a doua varianta ar fii cea mai buna pentru codare
x = my_function()
print(x)
# ctrl z undo si ctrl/
p_1r = 33
p_2r = 35
# PI = 3.14      # in programare constantele se definesc cu litere mari exemplu valoarea lui pi
area_1r = pi * p_1r * p_1r
area_2r = pi * p_2r * p_2r

pizza_1 = 100
pizza_2 = 86

print(f"Prima pizza :  {area_1r / pizza_1}")
print(f"A doua pizza : {area_2r / pizza_2}")


