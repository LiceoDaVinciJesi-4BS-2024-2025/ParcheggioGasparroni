from veicolo import Veicolo

class Auto(Veicolo):
    def __init__(self,marca:str,modello:str,colore:str,cilindrata:int,alimentazione:str,targa:str,passmax:int,passeggeri:int,capmax:int,kgmerce:int):
        super().__init__(marca,modello,colore,cilindrata,alimentazione,targa)
            
        self.__passmax = (passmax)
        
        if passeggeri > self.__passmax:
            raise ValueError("Troppa gente")
        
        self.__passeggeri = passeggeri
        
        self.__capmax = capmax
        
        if kgmerce > self.__capmax:
            raise ValueError("Troppa droga")
        
        self.__kgmerce = kgmerce
    
    def __str__(self):
        auto = "Auto" + str(self.__dict__)
        return auto
    
    @property
    def passmax (self):
        return self.__passmax
    
    @property
    def passeggeri (self):
        return self.__passeggeri
    
    @passeggeri.setter
    def passeggeri (self,value):
        
        if passeggeri > self.__passmax:
            
            raise ValueError("Troppa gente")
        
        self.__passeggeri = value
        
        return
    
    @property
    def capmax (self):
        return self.__capmax
    
    @property
    def kgmerce (self):
        return self.__kgmerce
    
    @kgmerce.setter
    def kgmerce (self,value):
        
        if kgmerce > self.__capmax:
            
            raise ValueError("Troppa gente")
        
        self.__kgmerce = value
        
        return

if __name__ == "__main__":
    a1 = Auto("Ferrari", "Sf90", "rosso", 6000, "benzina", "BG999JW", 2, 1, 200, 70)
    print(a1)