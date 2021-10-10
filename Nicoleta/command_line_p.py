import sys

print(sys.argv)


#Sa se scrie codul necesar pentru a alege limba romana din command line paramenter
#limba va fi primul parametru, valoarea romana sau english
import sys
if len(sys.argv) > 1:
    print(sys.argv)
    language = sys.argv[1]
else:
    # print(f'Please select a language')
    language = input('Please select a language')
if language == 'english':
    input_cmd_msg = "Please input a command: "
    a_cmd_msg = "You chose a"
else:
    input_cmd_msg = "Introduceti o comanda: "
    a_cmd_msg = "Ati ales a"



command = input(input_cmd_msg)
while command != 'q':
    if command == 'a':
        print(a_cmd_msg)
    command = input(input_cmd_msg)
