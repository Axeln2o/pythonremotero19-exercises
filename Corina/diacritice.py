# fiind dat un text in limba romana (cu diacritice), sa se scrie o functie care converteste literele cu diacritice in litere fara diacritice, si returneaza textul modificat.
def conv_diac(text):
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
        elif character == "î":
            new_string += "i"
        else:
            new_string += character

    return new_string

text = "Bacău ( pronunție , supranumit și „orașul lui Bacovia”) este municipiul de reședință al județului cu același nume, Moldova, România."
print(conv_diac(text))

#exemplu 2
text = 'George Bacovia (născut George Andone Vasiliu) n. 4/16 septembrie 1881, Bacău, România – d. 22 mai 1957,[2][3][4][5] București, România) '
def conv_diac(txt):
    diacritice = {'ă': 'a', 'ș': 's', 'ț': 't', 'î': 'i', 'â': 'a'}
    for lit in txt:
        if lit in diacritice:
            txt = txt.replace(lit, diacritice[lit])
    return txt

print(text)
print(conv_diac(text))