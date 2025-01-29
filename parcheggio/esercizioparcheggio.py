from veicolo import Veicolo
from auto import Auto
from moto import Moto
import datetime
from postomezzo import PostoMezzo

guadagno = 0

class Parcheggio(PostoMezzo):
    def __init__(self):
        super().__init__(posto,mezzo,dataPartenza)
        self.__parcheggiauto = 1000
        self.__parcheggimoto = 200
        
        file = open("park.data","w")
        file.write((f"Guadagno attuale:{guadagno}"))
        file.close()
        
    def __str__ (self):
        parcheggio = "Parcheggio" + str(self.__dict__)
        return parcheggio
    
    @property
    def parcheggiauto(self):
        return self.__parcheggiauto
    
    @property
    def parcheggimoto(self):
        return self.__parcheggimoto
    
    def occupaPosto(tipologia:str):
        if tipologia == "auto":
            
            if self.__posto == False and self.__parcheggiauto > 0:
                
                self.__posto = True
                self.__mezzo = mezzo
                self.__dataPartenza = dataPartenza
                self.__targa = targa
                self.__parcheggiauto += -1
                
                tempotrascorso = self.__dataPartenza - datetime.datetime.now
                tempotrascinore = (int(tempotrascorso.total_seconds())) // (60**2)
                pagamento = 1.5 * tempotrascinore
                guadagno += pagamento
                file = open("park.data","a")
                file.write = (str(Auto.__dict__))
                file.write = (f"Guadagno attuale:{guadagno}")
                file.close()
            elif self.__parcheggiauto <= 0:
                
                raise ValueError ("Posti auto terminati")
            
        elif tipologia == "moto":
            
            if self.__posto == False and self.__parcheggimoto > 0:
                self.__posto = True
                self.__mezzo = mezzo
                self.__dataPartenza = dataPartenza
                self.__targa = targa
                self.__parcheggimoto += -1
                
                tempotrascorso = self.__dataPartenza - datetime.datetime.now
                tempotrascinore = (int(tempotrascorso.total_seconds())) // (60**2)
                pagamento = 1.2 * tempotrascinore
                guadagno += pagamento
                file = open("park.data","a")
                file.write = (str(Moto.__dict__))
                file.write = (f"Guadagno attuale:{guadagno}")
                file.close()
            elif self.__parcheggimoto <= 0:
                
                raise ValueError ("Posti moto terminati")
    def liberaPosto(self,tipologia:str):
        if tipologia == "auto":
            if self.__posto == True and datetime.datetime.now == self.__dataPartenza:
                self.__posto == False
                self.__mezzo ==  None
                self.__dataPartenza = None
                self.__targa = None
                self.__parcheggiauto += 1
                
                
                
        if tipologia == "moto":
            if self.__posto == True and datetime.datetime.now == self.__dataPartenza:
                self.__posto == False
                self.__mezzo ==  None
                self.__dataPartenza = None
                self.__targa = None
                self.__parcheggiauto += 1

if __name__ == "__main__":
    a1 = Auto("Ferrari", "Sf90", "rosso", 6000, "benzina", "BG999JW", 2, 1, 200, 70)
    p1 = Parcheggio(posto=True , mezzo=a1 , dataPartenza = datetime.datetime(2025, 7, 20, 20, 18, 00))
    print(p1)
    print(p1.occupaPosto(a1,datetime.datetime(2025, 7, 20, 20, 18, 00),"BG999JW","auto"))
    print(p1)
    print(p1.liberaPosto("auto")
    print(p1)
