class Car:
    def __init__(self,naw): # Em Regeye bekardet bo kwrtkrdnewe, herweha eshi eweye her katek instance k drwst
        #bet em print dekat, leber ewe leme pewystman be SetOwner ye yekser eme dadeneyn w nawekan le naw class pey
        #dedeyn.
        self._naw=naw
    def GetOwner(self): #self ya3ny aw instance ey ke esta hete.
        print("Owner is ",self._naw)


def main():
    mycar=Car("jwtiyar") #eme kopyeke le class eke (instance)
    mycar.GetOwner() #Eme bo bangkrdny class e serekyekeye.
    kerimcar = Car("cemil") #besheky trt zyad krd bo kaseky tr beheman taybetmendy class y sereky.
    kerimcar.GetOwner()


if __name__ == '__main__':main()