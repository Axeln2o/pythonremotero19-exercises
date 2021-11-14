
##Math3 este un modul creat doar pentru a face demonstatia de mai jos, el nu s-a aflat in informatia initiala, adica celelalte module existente

import sys   # Aceasta este o modalitate de a importa o informatie dint-un package in alt package
          # Math3 se afla in `examplepackage` iar informatia importata este din `exercise2`
sys.path.append(r"C:\Users\gheor\PycharmProjects\pythonremotero19-exercises\Alex\exercise 2")
import SDAMath
from SDAMath import Mathsecu
from SDAMath.Mathsecu import div as imp
print(imp(12, 6))


