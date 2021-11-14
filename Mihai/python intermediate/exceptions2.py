result=None

try:
    a=int(input("a="))
    b=int(input("b="))
    result=a/b

except ZeroDivisionError:
    print("B este 0 si nu putem imparti!")

except ValueError:  #Value error este predefinita in python
                    #Va intra pe acesta ramura cand a sau b nu se pot converti la int
        print("Unul dintre numerele a sau b nu poate fii convertit la int!")
except:
    #Pe aceasta ramura va intra cand apare orice alta eroare in afara de ZeroDivisionError si ValueError
    print("Another errror eccured!")

print(f"rezultatul este :{result}")