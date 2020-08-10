def main():
    # Loop control le nawekey dyare bo kontroll krdny loop e, dyarydekat ke for loop chybkat chy nakat
    #le katy cebecekrdny condition, 3 frman heye bo loop (break, continue, pass)
    #break= wate frmaneke bwastene w berdewam mebe
    #continue= wate derry dway xot print meke w bgerrewe bo for .
    #pass= bo eweye boshay bejebellyt le naw bernameke ke run debet.
    print("======= Break =======")
    wshe="kurdistan"
    for pyt in wshe:
        print(pyt)
        if(pyt=='t'):
            break #ta pyty t achet w dadexretawa.
    print("======= Continue =======")
    for pyt in wshe:
        if(pyt=='t'):
            continue #lera pey dalle ka pyt=t ewe yekser bgerrewa bo for.
        print(pyt)
    print("======= Pass =======")
    for pyt in wshe:
        if(pyt=='t'):
            pass #leraya hy4 shtek nakat wakw bejeheshtn, print('bahse') bes bo bynyny eshakaya agina agar
            #naynwsy hy4 darnakawe.
            print("bashe")
        print(pyt)
    print("dawaname tewaw bw")

if __name__ == '__main__':main()