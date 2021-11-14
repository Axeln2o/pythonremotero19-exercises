"""
Entering examplepackage/__init__.py
Acest fisier se va executa de fiecare data cand se va apela functia `import examplepackage`.
"""
from .functions import list_symbols, is_symbol
from .symbols import *

print(__doc__)   # acest `print doc` va printa tot ce se va scrie mai sus in triple ghilimele
                   # fara init si main, folderul nu poate fi considerat un package
