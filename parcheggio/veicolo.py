listamarche = ["Ferrari","Lamborghini","Bugatti","McLaren","Rolls Royce","Bentley","Koenigsegg","Maybach","Ducati","Yamaha","KTM","Honda"]
listacolore = ["nero","rosso","giallo","verde","carbonio"]
listaalimentazione = ["benzina","diesel","elettrico","ibrido"]
alfabeto = "QWERTYUIOPASDFGHJKLZXCVBNM"
numeri = "1234567890"

class Veicolo:
    def __init__(self,marca:str,modello:str,colore:str,cilindrata:int,alimentazione:str,targa:str):
        
        if marca not in listamarche:
            raise ValueError ("Marca non borghese")
        
        self.__marca = marca
        
        self.__modello = modello
        
        if colore not in listacolore:
            raise ValueError ("Colore non accettato")
        
        self.__colore = colore

        if (cilindrata % 100) != 0:
            raise ValueError ("Cilindrata non accettata")
        
        self.__cilindrata = cilindrata
        
        if alimentazione not in listaalimentazione:
            raise ValueError ("Alimentazione non accettata")
            
        self.__alimentazione = alimentazione
        
        if len(targa) != 7 or targa[0] not in alfabeto or targa[1] not in alfabeto or targa[2] not in numeri or targa[3] not in numeri or targa[4] not in numeri or targa[5] not in alfabeto or targa[6] not in alfabeto:
            
            raise ValueError("ERRORE")
        
        self.__targa = targa
    
    def __str__(self):
        veicolo = "Veicolo:" + str(self.__dict__)
        return veicolo
    
    @property
    def targa(self):
        return self.__targa
    
    @targa.setter
    def targa(self,value):
        
        if len(targa) != 7 or targa[0] not in alfabeto or targa[1] not in alfabeto or targa[2] not in numeri or targa[3] not in numeri or targa[4] not in numeri or targa[5] not in alfabeto or targa[6] not in alfabeto:
            
            raise ValueError("ERRORE")
        
        self.__targa = value
        
        return
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,value):
        if marca not in listamarche:
            raise ValueError ("Marca non borghese")
        
        self.__marca = value
        
        return
    
    @property
    def colore(self):
        return self.__colore
    
    @colore.setter
    def colore(self,value):
        if colore not in listacolore:
            raise ValueError ("Colore non accettato")
        
        self.__colore = value
        
        return
    
    @property
    def alimentazione(self):
        return self.__alimentazione
    
    @alimentazione.setter
    def alimentazione(self,value):
        if alimentazione not in listaalimentazione:
            raise ValueError ("Alimentazione non accettata")
        
        self.__alimentazione = value
        
        return
    
    @property
    def cilindrata(self):
        return self.__cilindrata
    
    @cilindrata.setter
    def cilindrata(self,value):
        if (cilindrata % 100) != 0:
            raise ValueError ("Cilindrata non accettata")
        
        self.__cilindrata = value
        
        return
    
    @property
    def modello(self):
        return self.__modello
    
    def __le__ (self,other):
        if self.__marca <= other.marca:
            return True
        elif self.__modello <= other.modello:
            return True
        elif self.__cilindrata <= other.cilindrata:
            return True
    
if __name__ == "__main__":
    v1 = Veicolo("Ferrari", "Sf90", "rosso", 6000, "benzina", "BG999JW")
    print(v1)
    v2 = Veicolo("Lamborghini","Aventador SVJ","nero",7200,"benzina","GG009BB")
    print(v2)
    print(v1.__le__(v2))