def main():  #bangkrdny file w drwstkrdny file
    perrge=open("perrge.txt","a") # Eger "w" bet ewe her destkaryke bkey ewaney peshw desrretewe, beLamm
    #eger wystt ewaney peshw nesrretwa ewa deykey be "a"
    perrge.write("Chony")
    perrge.write("\nChaky")
    perrge.close()   #Hemw kat debet file dabxayt.
    Xwendnewe=open("perrge.txt","r")
    for derr in Xwendnewe:
        print(derr)
    Xwendnewe.close()

    kagaz=open("testy.txt","a")
    kagaz.write("CHony \nchaky ")
    kagazxwendnewe=open("testy.txt","r")
    for der in kagazxwendnewe:
        print(der)
    kagazxwendnewe.close()

if __name__ == '__main__':main()