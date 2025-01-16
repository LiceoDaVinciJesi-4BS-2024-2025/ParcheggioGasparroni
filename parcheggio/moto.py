from veicolo import Veicolo

class Moto(Veicolo):
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
        moto = "Moto" + str(self.__dict__)
        return moto
    
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
    m1 = Moto("Ducati", "Panigale", "rosso", 1000, "benzina", "BG999JW", 2, 1, 150, 64)
    print(m1)