#Ce capabilitati are un telefon:
#face poze
#poti suna
#navigare online
#GPS
#VIDEO

#ce face un smart TV:
#navigare online
#emisiuni
#cablu tv
#video

#ce face smart-watch
#poti suna
#numara pasi
#health monitoring
#health monitoring

class GPS:
    def get_possition(self):
        print("Getting the current position")

class Video:
    def run_video(self):
        print("Running current video")

class Calling:
    def calling_person(self):
        print("Call me baybe!")

    def answer_call(self):
        print("Wrong number")

class Health:
    def heart_rate(self,number_beats_per_sec):
        if number_beats_per_sec>=200:
            print("You are having a heart-attack!")
        else:
            print("You are oke!")

    def numara_pasi(self,step_perday):
        if step_perday == 10000:
            print("Congrats!")
        else:
            print("Now you have to do some more steps")



class Cablutv:
    def setare_canal(self):
        print("Canalul dorit este setat!")


class NavigareOnline:
    def open_chrome(self):
        print(f"Canalul dorit este setat!")

class Foto:
    def take_pic(self):
        print("The picture was taken!")

class Telefon(GPS,Video,Calling,NavigareOnline,Foto):

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def take_pic(self):
        print("The hd photo was taken!")

class SmartTV(Video,NavigareOnline,Cablutv):

    def __init__(self,brand,rezolutie):
        self.brand=brand
        self.rezolutie=rezolutie

    def setare_canal(self):
        print("Fara semnal-404!")

class SmartWatch(GPS,Calling,Health):
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def calling_person(self):
        print("The person is not reachable ! ")


if __name__=="__main__":
    #creearea instantelor a claselor
    telefon=Telefon("hiphone","12")
    tv=SmartTV("Samsung","1024x560")
    watch=SmartWatch("OPPO","X1")
    telefon.take_pic()
    telefon.run_video()
    telefon.calling_person()
    tv.setare_canal()
    tv.open_chrome()
    watch.numara_pasi(1000)





