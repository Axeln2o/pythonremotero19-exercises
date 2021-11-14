from datetime import datetime

def disable_at_night(func):#func este un alias generic pt o functie pe care se va aplica decoratorul

    def wrapper():# spun ce face disable at night
        t=datetime.now() #cat este timpul acum
        if t.hour>=8 and t.hour<=9:#Daca este timp de zi
            func() #chem functia la care a fost utilizat decoratorul
        else:
            print(f"It's night!Function can not run!")
    return wrapper

#Mersi frumos ! :)

@disable_at_night
def hello():
    print("Hello world!")

if __name__=="__main__":
    hello()