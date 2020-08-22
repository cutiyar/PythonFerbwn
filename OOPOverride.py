#krdary Override w Super
class operation():
    def Sum(self,n1,n2):
        SumEncam=n1+n2
        print("Sum=",SumEncam)
    def Sub(self,n1,n2):
        Subencam=n1-n2
        print("Sub =",Subencam)
class OperationMul(operation):
    def mul(self,n1,n2):
        MulEncam=n1*n2
        print("Mul=",MulEncam)
    def Sub(self,n1,n2): #Eme heman Sub y class y peshwe, eme pey dewtret override, wate ew condtiton tetbyq
        #ekat ke inheritance (bomaweyiye), be manay tr bomaweke dexate pesh class y bawk.
        super().Sub(10,10) #Bem sheweye detwany bangy sub naw class y operation bkeyt.
        Subencam=n1-n2+5
        print("Sub =",Subencam)
def main():
    OP=operation()
    OP.Sub(10,10) #Emyan yekem sub y jebecekrdwe.
    OPmul=OperationMul()
    OPmul.Sum(10,10)
    OPmul.Sub(10,10)
    OPmul.mul(10,10)

if __name__ == '__main__':
    main()