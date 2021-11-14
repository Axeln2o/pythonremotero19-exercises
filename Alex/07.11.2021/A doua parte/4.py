#Write a decorator that will show the hour, minute and second before calling the code of the decorated
# function and after calling the code of the decorated function.

from datetime import datetime


def before_after_calling(func):
    def wrapper(*args, **kwargs):
        print(f"Timpul intial este: {datetime.now().strftime('%H:%M:%S')}.")
        func(*args, **kwargs)
        print(f"Timpul final este: {datetime.now().strftime('%H:%M:%S')}")

    return wrapper




@before_after_calling
def sum_total(salar):
    a = 0
    for i in range (12870000):
        a = salar*salar*salar
    print(f" Salariul anual este de: {a}.")

if __name__== "__main__":
    sum_total(1500)

