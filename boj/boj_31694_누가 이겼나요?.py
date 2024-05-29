import sys; sys.stdin = open("31694.txt", "r")

Algosia = list(map(int, input().split()))
Bajtek = list(map(int, input().split()))

if sum(Algosia) != sum(Bajtek):
    if sum(Algosia) > sum(Bajtek):
        print("Algosia")
    else:
        print("Bajtek")
    exit()
flag = False
for i in range(10, 0, -1):
    if Algosia.count(i) > Bajtek.count(i):
        print("Algosia")
        flag = True
        break
    elif Bajtek.count(i) > Algosia.count(i):
        print("Bajtek")
        flag = True
        break
if flag == False:
    print("remis")
