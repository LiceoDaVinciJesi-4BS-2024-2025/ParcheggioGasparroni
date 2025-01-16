mezziaccettati = ["moto","auto"]

class PostoMezzo:
    def __init__(self):
        self.__parcheggiauto = 700
        
        self.__parcheggimoto = 200
        
    def __str__(self):
        
        posti = "Posti" + str(self.__dict__)
        
        return posti
    
    @property
    
    def parcheggiauto(self):
        
        return self.__parcheggiauto
    
    @property
    
    def parcheggimoto(self):
        
        return self.__parcheggimoto
    
    def occupaPosto(self,tipologiamezzo):
        if tipologiamezzo.lower() not in mezziaccettati:
            
            raise ValueError("Accettiamo solo moto e auto")
        
        if tipologiamezzo.lower() == "moto" and self.__parcheggimoto >= 1:
            self.__parcheggimoto += -1
            
            
        elif tipologiamezzo.lower() == "auto" and self.__parcheggiauto >= 1:
            self.__parcheggiauto += -1
            
    
    def liberaPosto(self,tipologiamezzo):
        if tipologiamezzo.lower() not in mezziaccettati:
            
            raise ValueError("Accettiamo solo moto e auto")
        
        if tipologiamezzo.lower() == "moto" and self.__parcheggimoto >= 1:
            self.__parcheggimoto += 1
            
        elif tipologiamezzo.lower() == "auto" and self.__parcheggiauto >= 1:
            self.__parcheggiauto += 1
            

if __name__ == "__main__":
    p = PostoMezzo()
    print(p)
    print(p.occupaPosto("auto"))
    print(p)
    print(p.liberaPosto("auto"))
    print(p)
    
