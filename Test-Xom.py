'''import datetime

Dayk = input("tement bnwse: ")
sall = datetime.datetime.now().year
zhyan = sall-int(Dayk)
print("tement {}, be dllnyayewe sally dahatww debyte {} be xembe".format(zhyan, zhyan+1))
print("Leber ewe Gwe mede dnya")

'''
'''''# Emesh danyeky tre her leser if w else w condition detwany aw se quote labay w run y bkayt.
def main():
    Tomen= input("Tement bnwse: ")  #hibb
    if (int(Tomen)>5 and int(Tomen)<10):
        print("To pyaweki meqwlly")
    elif (int(Tomen)>10 and int(Tomen)<15):
        print("To Teenage")
    elif (int(Tomen)>15 and int(Tomen)<20):
        print("To peghashtwy")
    elif (int(Tomen)>20 and int(Tomen)<25):l
        print("pyaweky maqwly kake")

    else:
        print("to jare mawte")

    print("Esta dadexretawa")

if __name__ == '__main__':main() '''

def main(): #Em nmwneye bo eweye bzany detwanret naw blok of code chendyn condition w functiony try tyabet. wekw
    #if le naw if, yan break,while,for,in
    #lew block of code detwanret chenha string w beshy try tyabet
    Tomen= input("Tement bnwse: ")  #hibb
    if (int(Tomen)>5 and int(Tomen)<10):
        if(int(Tomen)>7):
            print("to ma3qwl tri")
        else:
            print("to myaqeky ma3qwlyi")

if __name__ == '__main__':main()