def main(): #Exceptions bekardet bo ancamdany karek beserkewtwwy eger nebww peuyamekt bo bejebellet ke
    #ke pet blle hellekey to le kweye, ke nahellet bernameke Excute bkat. wek srrynewey failek ke pewsyte
    #bo bnernamekey toy bellam srrawetewe.
    try:
        Xwendnewe = open("perrge.txt", "r")
        for derr in Xwendnewe:
            print(derr)
        Xwendnewe.close()
    except IOError: #Chend corek helle heye detwany le error w exception le python.org hamwy bbyny kamey
        #to pewystt peyaty w penasay eshekey to dekat.
        print("Perrge bwny nye")

    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
if __name__ == '__main__':main()