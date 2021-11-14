
import time
import functools


def cronometru(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # do the magic here
        t1 = time.time()
        y = func(*args, **kwargs)
        t2 = time.time()
        print(f"A durat {t2 - t1} secunde!")
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
def g(x):
    y = None
    for i in range(10000000):
        y = x ** x + 2*x
    return y


if __name__ == "__main__":
    f(10)
    g(10)
    #f(10)
    #t1 = time.time()
    #f(13)
    #t2 = time.time()
    #print(f"A durat {t2 - t1} secunde!")