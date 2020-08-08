import datetime
def main():
    Ledaykbwn=input("Tement bnwse:")
    Year=datetime.datetime.now().year
    Temen= Year-int(Ledaykbwn)
    print("Tement brytye le {} sall ".format(Temen))
    if(int(Temen)>18):
        print("Bexer haty")
    else:
        print("jare bebeyt")

    print("Dawanameke Dadexretewe")
if __name__ == '__main__':main()