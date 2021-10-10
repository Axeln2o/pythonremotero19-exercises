# Sa se scrie codul necesar pentru a alege limba din command line paramenter.
# limba va fi primul parametru, valoarea romana sau english
import sys
if len(sys.argv) > 1:

    print(sys.argv)# am printat lista sys.argv care contine 2 elemente: fisier si "english"
# cand trecem in termina python .\command_line.py romana imi ia romana
#putem capta orice parametru dupa numele fisierului cu acest print(sys.argv)
    language = sys.argv[1]
else:
    # print(f'PLease select a language')
    language = input("Please select a language: ")
if language == 'english':
    input_cmd_msg = "Please input a number: "
    a_chosen_msg = "You chose a"
else:
    input_cmd_msg = "Introduceti o comanda: "
    a_chosen_msg = "Ati ales a"

command = input(input_cmd_msg)
while command != 'q':
    if command == 'a':
        print(a_chosen_msg)
    command = input(input_cmd_msg)


#Shift+F6 face replace/ refactor- inlocuieste variabila respectiva peste tot pe unde o intalneste
