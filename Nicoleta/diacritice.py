## Fiind dat un text in limba romana (cu diacritice), sa se scrie o functie care converteste literele
# cu diacritice in litere fara diacritice, si returneaza textul modificat.

def convert_diac(text):
    print(text)
    new_string = ""
    for character in text:
        if character == "ă":
            new_string += "a"
        elif character == "ț":
            new_string += "t"
        elif character == "ș":
            new_string += "s"
        elif character == "â":
            new_string += "a"

        else:
            new_string += character

    return new_string


text = "Bacău ( pronunție , supranumit și „orașul lui Bacovia”) este municipiul de reședință al județului cu același nume, Moldova, România"

print(convert_diac(text))
