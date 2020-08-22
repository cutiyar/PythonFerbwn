class Car:
    def GetOwner(self): #self ya3ny aw instance ey ke esta hete.
        print("Owner is ",self._naw)
    def SetOwener(self,naw): #Lere tenha peman wt her SetOwner hat naweke werbgre w daxly ke.
        self._naw=naw

def main():
    mycar=Car() #eme kopyeke le class eke (instance)
    mycar.SetOwener("Gara")
    mycar.GetOwner() #Eme bo bangkrdny class e serekyekeye.
    kerimcar = Car() #besheky trt zyad krd bo kaseky tr beheman taybetmendy class y sereky.
    kerimcar.SetOwener("Nali")
    kerimcar.GetOwner()


if __name__ == '__main__':main()