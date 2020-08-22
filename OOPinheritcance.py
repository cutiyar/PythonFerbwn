#lem beshe basy inheritance
class operation():
    def Sum(self,n1,n2):
        SumEncam=n1+n2
        print("Sum=",SumEncam)
    def Sub(self,n1,n2):
        Subencam=n1-n2
        print("Sub =",Subencam)
class OperationMul(operation): #Lerewe detwany be class e bashek zyad bkey bo class y peshw, eme pey dellen
    #Inheritance wate bomaweyy, wate ew beshey classy peshwsh bekardene be nwsyny operation le naw operationMUL
    #wate bangy operation bke w eme class bde be demy ewewe.
    def mul(self,n1,n2): #emesh bw be beshek le class y peshw.
        MulEncam=n1*n2
        print("Mul=",MulEncam)
def main():
    OP=operation() #lere penaseman krd bo ewey bangy yekem class bkat.
    OPmul=OperationMul();
    OPmul.Sum(10,10)
    OPmul.Sub(10,10)
    OPmul.mul(10,10)

if __name__ == '__main__':
    main()