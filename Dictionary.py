def main():
    # la dic atwany chand key w value yak dabney bo penasakrdny shtek
    #barrez={"naw":"jwtyar","temen":30}
    #atwany ba hsewaya trysh dic drwst bkay wak amay xwarawa:
    barrez= dict(naw="jwtiyar")
    barrez['esh']="krekar" # Atwany danayak zyad bkay bo dict. labaraway mutable.

    print(barrez,type(barrez))
    print(barrez['naw'])
    #barrez.clear() #Ba Clear hamw dict yaka pak dakayatwa.
    #print(barrez, type(barrez))

if __name__ == '__main__':main()