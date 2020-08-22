import OOPbasicClass #Lerewe bangy file ky trman krd ke xoman drwstman krdwe.
#Bes ew beshe bang dekat ke main nye wate ewey pesh main(), chwnke ew beshey naw main tenha
#ew kate excute debet eger run bkret le naw fily xoy.

def main():
    car=OOPbasicClass.Car() #Lere bangy file ekeman krd w enja instance ekey.
    car._naw="Karos" #Car peman wt ew nawe wergret.
    car.GetOwner() #GetOwner le file daman nawe kr printy naweke bkat.
    car.SetOwener("Galla") #Bem sheweyesh etwany le SetOwner ewe naweke banbkeyt.
    car.GetOwner()
if __name__ == '__main__':
    main()