# Slice bo dast gayshtna ba zanyaryakan ba shewayaky xera
def main():
    lis = [1, 2, 4, 45, 3, 343, 4]
    print(lis[3])
    lis[:] = range(10)  # Agar bmawe item zyad bkam bo listaka, bo nmwna la 1 ta 9 zyad bka ka dakata 10.
    print(lis)
    x = lis[2:7]
    print(x)
    x = lis[0:4] = (0, 0, 0, 0)
    print(x)
    print("hi")
    lis[:]=range(100)
    print(lis)
    lis[0:4] = (0, 0, 0, 0) # Bam Shewaya datwany shwenakan jegorrke pe bkayt.
    print(lis)
if __name__ == '__main__': main()
