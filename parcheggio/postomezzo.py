from veicolo import Veicolo
from auto import Auto
from moto import Moto
import datetime

class PostoMezzo:
    def __init__(self):
        self.__posto = False
            
        self.__mezzo = None

    def __str__(self):
        posto = "Posto:" + str(self.__dict__)
        return posto
    
    @property
    def mezzo(self):
        return self.__mezzo
    
    @property
    def posto(self):
        return self.__posto
      
    def occupaPosto(self , mezzo:Veicolo, dataPartenza:datetime,targa:str):
        if self.__posto == False:
            self.__posto = True
            self.__mezzo = mezzo
            if dataPartenza <= datetime.datetime.now():
                raise ValueError("Orario non disponibile")
            self.__dataPartenza = dataPartenza
            self.__targa = targa
            return ("Posto preso")
        if self.__posto == True:
            raise ValueError("Posto occupato")

    def liberaPosto (self):
        if self.__posto == True:
            self.__posto = False
            self.__mezzo =  None
            self.__dataPartenza = None
            self.__targa = None
            return ("Posto libero")
    

if __name__ == "__main__":
    a1 = Auto("Ferrari", "Sf90", "rosso", 6000, "benzina", "BG999JW", 2, 1, 200, 70)
    a2 = Auto("Lamborghini","Aventador","nero",5400,"benzina","GG300CK", 2, 2, 250, 130)
    posto = PostoMezzo()
    print(posto)
    print(posto.occupaPosto(a1,datetime.datetime(2025, 7, 20, 20, 18, 00),"BG999JW"))
    print(posto)
#    print(posto.occupaPosto(a2,datetime.datetime(2025, 8, 17, 21, 00, 00),"GG300CK"))
#    print(posto)
    print(posto.liberaPosto())
    print(posto)

            










