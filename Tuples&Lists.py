def main():
    print("================ TUPLES ===================")
    temen=(23,24,25,26) #tuples immutable wata natwanre daskary bkre hy4y bo zya bkre.
    print(temen,type(temen)) #lera peman alle jory tuples a chwnka naw kawnaaya.
    print(temen[0]) #lera bas yakam jmare print akat.
    print(temen[0:3])  # lera la 0 print aka ta 2, 3 yaka print naka wata ta 2 brro 3 shmwl naka pey alle 3 xtwa brro
    # wate 0,1,2.

    #temen.index()
    #temen.count()

    print("================ LIST =====================")
    # List mutable a wata atwany list aka gorrankary bo bkey .
    # atwanyn list bkayna naw list
    #datwanyn bam sjewayash dyary bkayn [0:] aw kata la sfrawa ta kotay print aka
    #ba 3asksyshawa atwanyn dyary bkayn ch zhmaraya print bka ba naqs (-5,-4,-3,-2,-1).

    temeni=[12,13,14,15]
    temeni.append(34)  #lera twanyman daskary list aka bkayn w basheky try bo zya bkayn.
    temeni.insert(2,22) #lera pey allen la fllan shwen fllan shtman bo zya bka ba insert.
    temeni.pop(2)  #zhmara 2 y ryzaka dar akat agar dyary nakay axyr dana dar akat.
    temeni.remove(12)
    temeni.extend([29,34,55])  # bama atwany chan danayak zya bkay bo listaka
    #max() , min() , sum()  #datwany amanash bakar beny.
    print(temeni,type(temeni))
    print(temeni[2])
    print(temeni[0:2])

    # Em dyary krdni shwena bo string ekysh har haman 3amalayaya

    print("================= String ================")
    esht="Quality Oontrol"
    print(esht[0:2]) # ta dwam danay krd .
    print(esht[2:3]) # 2 agretawa bas 3 nagretawa

    #lera basy Set akayn

    print("================== SET ===================") #la SET natwanyn index bkayn chwnka zhamarakan randomn
    qalb ={2,3,4,5,6}
    print(qalb,type(qalb))
if __name__ == '__main__':main()