listamarche = ["Ferrari","Lamborghini","Bugatti","McLaren","Rolls Royce","Bentley","Koenigsegg","Maybach"]
listacolore = ["nero","rosso","giallo","verde","carbonio"]
listaalimentazione = ["benzina","diesel","elettrico","ibrido"]


class Veicolo:
    def __init__(self,marca:str,modello:str,colore:str,cilindrata:int,alimentazione:str,targa:str):
        self.__marca = marca
        self.__modello = modello
        self.__colore = colore
        self.__cilindrata = cilindrata
        self.__alimentazione = alimentazione
        self.__targa = targa
    
    def __str__(self):
        veicolo = "Veicolo:" + str(self.__dict__)
        return veicolo
    
    @property
    def targa(self):
        return self.__targa
    
    @targa.setter
    def targa(self,value):
        alfabeto = "QWERTYUIOPASDFGHJKLZXCVBNM"
        numeri = "1234567890"
        if len(value) != 7 or value[0] not in alfabeto or value[1] not in alfabeto or value[2] not in numeri or value[3] not in numeri or value[4] not in numeri or value[5] not in alfabeto or value[6] not in alfabeto:
            raise ValueError("lunghezza targa errata")
        
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
    
    @marca.setter
    def colore(self,value):
        if colore not in listacolore:
            raise ValueError ("Colore non accettato")
        
        self.__colore = value
        
        return
    
    @property
    def alimentazione(self):
        return self.__alimentazione
    
    @marca.setter
    def alimentazione(self,value):
        if alimentazione not in listaalimentazione:
            raise ValueError ("Alimentazione non accettata")
        
        self.__alimentazione = value
        
        return
    
    @property
    def cilindrata(self):
        return self.__cilindrata
    
    @marca.setter
    def cilindrata(self,value):
        if (cilindrata % 100) != 0:
            raise ValueError ("Cilindrata non accettata")
        
        self.__cilindrata = value
        
        return
    
    @property
    def modello(self):
        return self.__modello
    
    def __lt__(self,other):
        