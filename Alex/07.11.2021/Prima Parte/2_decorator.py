from datetime import datetime


def disable_at_night(func):  # func este un alias generic pentru o functie pe care se va aplica decoratorul

    def wrapper():  # prin wrapper spun ce face functia 'disable at night'
        t = datetime.now()  # retinem cat este timpul/ceasul acum
        if t.hour >= 8 and t.hour <= 22:  # daca este pe timp de zi
            func()  # chem functia la care a fost utilizat decoratorul
        else:
            #altfel, dam ceasul
            print("It's night! Function cannot be run!")
    return wrapper



@disable_at_night
def hello():
    print("Hello World!")


if __name__ == "__main__":
    hello()
