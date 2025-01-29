from veicolo import Veicolo
from auto import Auto
from moto import Moto
import datetime

class PostoMezzo:
    def __init__(self , posto:bool,mezzo:Veicolo,dataPartenza: datetime.datetime):
        self.__posto = posto

        if posto == True and mezzo != None:
            
            self.__mezzo = mezzo
            
        elif posto == False:
            
            raise ValueError("Parcheggio libero")

        if dataPartenza > datetime.datetime.now():
            self.__dataPartenza = dataPartenza
        
        else:
            raise ValueError("Inserire un orario di uscita dopo quello attuale")

    def __str__(self):
        posto = "Posto:" + str(self.__dict__)
        return posto
    
    @property
    def mezzo(self):
        
        return self.__mezzo
    
    @property
    def posto(self):
        
        return self.__posto
    
    @property
    def dataPartenza(self):
        
        return self.__dataPartenza
    
    @dataPartenza.setter
    def dataPartenza(value):
        
        if value < datetime.datetima.now:
            
            raise ValueError("Inserire un orario di uscita dopo quello attuale")
        
        self.__dataPartenza
        
        return
    
        
    def occupaPosto(self , mezzo:Veicolo, dataPartenza,targa:str):
        if self.__posto == False:
            self.__posto = True
            self.__mezzo = mezzo
            self.__dataPartenza = dataPartenza
            self.__targa = targa
            
        return ("Posto preso")

    def liberaPosto (self):
        if self.__posto == True and datetime.datetime.now == self.__dataPartenza:
            self.__posto == False
            self.__mezzo ==  None
            self.__dataPartenza = None
            self.__targa = None
    

if __name__ == "__main__":
    a1 = Auto("Ferrari", "Sf90", "rosso", 6000, "benzina", "BG999JW", 2, 1, 200, 70)
    posto = PostoMezzo(posto=True , mezzo=a1 , dataPartenza = datetime.datetime(2025, 7, 20, 20, 18, 00))
    print(posto)
    print(posto.occupaPosto(a1,datetime.datetime(2025, 7, 20, 20, 18, 00),"BG999JW"))
    print(posto)
    print(posto.liberaPosto())
    print(posto)
            










