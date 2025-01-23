from datetime import datetime

from datetime import timedelta

alfabeto = "QWERTYUIOPASDFGHJKLZXCVBNM"
numeri = "1234567890"
mezziaccettati = ["moto", "auto"]

class PostoMezzo:
    def __init__(self):
        
        self.__parcheggimoto = 1
        
        self.__parcheggiauto = 1
        
        self.__postioccupati = {}

    def __str__(self):
        return "PostoMezzo:" + str(self.__dict__)
    
    @property
    
    def parcheggimoto(self):
        return self.__parcheggimoto

    @property
    
    def parcheggiauto(self):
        return self.__parcheggiauto

    def occupaPosto(self, tipologiamezzo:str , targa:str , ore:int):        
        if tipologiamezzo.lower() not in mezziaccettati:
            raise ValueError("Tipologia di mezzo non valida")
        
        if len(targa) != 7 or targa[0] not in alfabeto or targa[1] not in alfabeto or targa[2] not in numeri or targa[3] not in numeri or targa[4] not in numeri or targa[5] not in alfabeto or targa[6] not in alfabeto:
            
            raise ValueError("ERRORE")
        
        if targa in self.__postioccupati:
            raise ValueError("Veicolo già parcheggiato.")
        
        if ore <= 0:
            raise ValueError("Un po' ci devi stare")


        inizio = datetime.now()
        orariofine = inizio + timedelta(hours=ore)

        if tipologiamezzo == "moto":
            if self.__parcheggimoto > 0:
                
                self.__parcheggimoto += -1
                
                self.__postioccupati[targa] = (tipologiamezzo, inizio, orariofine)
                
            else:
                raise ValueError("Posti moto terminati")
        
        elif tipologiamezzo == "auto":
            
            if self.__parcheggiauto > 0:
                
                self.__parcheggiauto += -1
                
                self.__postioccupati[targa] = (tipologiamezzo,inizio, orariofine)
            else:
                raise ValueError("Posti auto terminati")

    def liberaPosto(self, targa):
        if len(targa) != 7 or targa[0] not in alfabeto or targa[1] not in alfabeto or targa[2] not in numeri or targa[3] not in numeri or targa[4] not in numeri or targa[5] not in alfabeto or targa[6] not in alfabeto:
            
            raise ValueError("ERRORE")
        
        if targa not in self.__postioccupati:
            
            raise ValueError("Targa non presente nel parcheggio")

        tipologiamezzo = self.__postioccupati.pop(targa)[0]

        if tipologiamezzo == "moto":
            
            self.__parcheggimoto += 1
           
        elif tipologiamezzo == "auto":
            
            self.__parcheggiauto += 1

if __name__ == "__main__":
    p = PostoMezzo()
    print(p)
    p.occupaPosto("auto", "AB123CD",1)
    print(p)
    p.liberaPosto("AB123CD")
    print(p)
