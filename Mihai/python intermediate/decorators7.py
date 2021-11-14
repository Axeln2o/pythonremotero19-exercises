#Write a decorator that will show the hour, minute and second before calling
# the code of the decorated function and after calling the code of the decorated function
from datetime import datetime

def before_after_calling(func):
    def wrapper(*args,**kwargs):
        print(f"Timpul initial este : {datetime.now().strftime('%m:%d:%h')}")
        func(*args,**kwargs)
        print(f"Timpul final, dupa apelul functiei este: {datetime.now().strftime('%m:%d:%h')}")
    return wrapper


@before_after_calling
def sum_total(salar_luna):
    s=0
    for i in range(120000):
        s=salar_luna*10000
    print(f"Salarul pe pe un an an este {s}")


if __name__=="__main__":
    sum_total(2000)