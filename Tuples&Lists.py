def main():
    print("===========TUPLES==============")
    temen=(23,24,25,26) #tuples immutable wata natwanre daskary bkre hy4y bo zya bkre.
    print(temen,type(temen)) #lera peman alle jory tuples a chwnka naw kawnaaya.
    print(temen[0]) #lera bas yakam jmare print akat.
    print(temen[0:3])  # lera la 0 print aka ta 2 3 yaka print naka wata ta 2 brro 3 shmwl naka pey alle 3 xtwa brro
    # wate 0,1,2.

    print("===========LIST================")
    # List mutable a wata atwany list aka gorrankary bo bkey .

    temeni=[12,13,14,15]
    temeni.append(34)  #lera twanyman daskary list aka bkayn w basheky try bo zya bkayn.
    temeni.insert(2,22) #lera pey allen la fllan shwen fllan shtman bo zya bka ba insert.
    print(temeni,type(temeni))
    print(temeni[2])
    print(temeni[0:2])

    # Em dyary krdni shwena bo string ekysh har haman 3amalayaya

    print("================= String =============")
    esht="Quality Oontrol"
    print(esht[0:2]) # ta dwam danay krd .

if __name__ == '__main__':main()