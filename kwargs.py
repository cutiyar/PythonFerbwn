class Car:
    #def __init__(self,naw):# bem seweye tenha yek nrxman dawe ewysh name, bellam em kare zor nerm nye bo eshkrdn,
        #chwnke eger chend variable k zyad bkem bo class eke esheke dwrw drezh deaktewe w yek nrx nye tenha naw bet.
        #boye swd le kwargs werdegryn
    def __init__(self,**kwargs):
        self.data=kwargs
    def GetOwner(self):
        print("Owner is ",self.data["Owner"])
        print("Model is ",self.data["Model"])
        print("Year ",self.data["year"])
    def Set_Model(self,Model): # Bem Sheweyesh detwany nrxeky tr zyad bkey.
        self.data["Model"]=Model
    def Get_Model(self):
        print("Model is ",self.data["Model"])

def main():
    mycar=Car(Owner="jwtiyar",Model="cadilac", year=2020) #Ler behoy kwarg detwany her nrxeky tr zyad bkeyt be asany.
    mycar.GetOwner()
    kerimcar = Car(Owner="cemil",Model="ford",year=2019)
    kerimcar.GetOwner()
    kerimcar.Set_Model("2016")
    kerimcar.Get_Model()

if __name__ == '__main__':main()