  # Sisteme de versionare, Python indexing, Module
  # Un package este o colectie de module, un modul este o colectie de functii sau de clase
  # Mai jos am invatat cum sa instalam Django si cum sa facem update la `pip`
  # Am facut toate updateurile in `Terminal`

'''
python --verion: prezint veriounea de python  ##am aflat asta jos in terminal dupa `>`
Python 3.7.4
X.Y.Z
X -> major revision: 
Y -> minor revision:
Z.-> Bug | Patch revision:

Pip - Managerul prin cae se intaleaza package-uri
PyPi - Locul sau Serverul de unde Pip aduce package-urile
1. python -m pip list                           :listeaza toate package
2. python -m pip install Django                 : instaleaza package-ul Django
3. python -m pip install Django==3.2.1          : instaleaza o versiune specifica
4. python -m pip install --upgrade Django       : aduce package-ul instalat la ultima versiune
5. python -m pip show Django                    : afiseaza informatii despre package-ul insalat
6. python -m pip uninstall Django               : Dezinstaleaza package-ul Django
7. python -m pip freeze >lista.txt              : genereaza o lista fizica cu toate package-urile instalate
8. python -m pip install -r lista.txt           : va parcurge lista si va instala fiecare package din ea
'''

  ##Virtual environment - un loc separat de sistemul nostru - un loc unde putem sa facem teste si experimente care sa nu ne afecteze buna functionare a calculatorului
  #Am reusit in CMD, nu a mers in PyCharm direct(cd ..., cd..., cd..., activate - si apare apoi la inceputul urmatorului rand (virtualENV)

'''
1. Pentru a crea un virtual envirnonment executam:
python -m venv"numeleEnvironmentului"
2. Trebuie ajuns in folderul `scripts` din cadrul lui:
 - fie din pycharm folosing comanda "cd"
 - fie din comand line
 - ! daca nu functioneaza din Pycharm folositi CMD
3. Executam comanda de `activate` pentru a activa Environmentul
4. Executam comanda de `deactivate` pentru a dezactiva Environmentul

'''

  ##Import

'''
1. Importam direct package-ul
import urllib 
# urllib.request.urlopen("https://google.com")

2. Importam direct modulul din package
import urllib.request   
# urllib.request.urlopen("https://amazon.com")

3. Importam direct modulul fara a importa package-ul
from urllib import request
# request.urlopen("https://ebay.com")

4. Importam direct functia de interes
from urllib.request import urlopen  
# urlopen("https://wikipedia.com")

5. Importarea tuturor functiilor din modul se face cu *
from urllib.request import* (* = importa tot din modul, exemplu: toate functiile sau toate clasele)
# urlopen("https://gmail.com")

6. importarea prin alias(as)
import graphicaluserinterface as gui

graphicaluserinterface.modul.func1
gui.modul.func1
'''