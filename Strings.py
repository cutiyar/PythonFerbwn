#Hemw shtek derbarey Strings

def main():
    data="SKllaw le ewe"

    x=data.lower()
    print(x)
    y=data.split() #jya krdnewe
    print(y)
    z=data.split("w") #le w wewe bom jya dekatewe.
    print(z)
    g=":".join(z)
    print(g)
    p=data.find("le") #Dozynewey shtek le string.
    print(p)
    print(data[7:9])
    o=data.capitalize() #eme bes pyty yekem capital dekat.
    print(o)
    u=data.islower() #Eger be lowercase bet True a, Eger Capital bet False dedat.
    print(u)
    i=data.count("le",1,11) #bekarder bo jmardny brrge le naw data., beshy dwemy pey dellet le pyty 1 dest
    #pebke ta pyty 11 le beyne bzane Chend "le" heye.
    print(i)
    txt = "My name is jwtyar"
    x = txt.encode() #be encode krdny wshe.
    print(x)
    k=txt.replace("j","l") #gorryny pyt.
    print(k)
    txt = "apple, banana, cherry"
    x = txt.rsplit(",") #string ekat be list be comma cyakrawe.
    print(x)




if __name__ == '__main__':main()