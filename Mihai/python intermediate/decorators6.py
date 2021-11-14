import time
import functools


def cronometru(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): #oricate argumente si oricare ar fii acestea
        # do the magic here
        t1 = time.time() #iau timpul in functie de apelul functiei func
        y = func(*args, **kwargs)
        t2 = time.time() #iau timpul dupa apelul functiei func
        print(f"A durat {t2 - t1} secunde!") #diferenta de timp
        return y
        # until here
    return wrapper


@cronometru
def f(x):
    y = None
    for i in range(10000000):
        y = x ** x
    return y


@cronometru
def g(x,y):
    y = y
    for i in range(10000000):
        z = x ** y + 2*x
    return y


if __name__ == "__main__":
    f(10)
    g(10,5)
    #f(10)
    #t1 = time.time()
    #f(13)
    #t2 = time.time()
    #print(f"A durat {t2 - t1} secunde!")