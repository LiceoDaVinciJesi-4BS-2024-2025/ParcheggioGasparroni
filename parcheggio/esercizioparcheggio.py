from postomezzo import PostoMezzo

class Parcheggio(PostoMezzo):
    def __init__(self):
        super().__init__(parcheggimoto,parcheggiauto,postioccupati)
        
    def prezzo(self):
        tipologiamezzo = self.__postioccupati(tipologiaMezzo)[0]