import sys; sys.stdin = open("30794.txt", "r")

lv, judgment = input().split()
if judgment == "miss":
    print(0)
elif judgment == "bad":
    print(int(lv) * 200)
elif judgment == "cool":
    print(int(lv)*400)
elif judgment == "great":
    print(int(lv)*600)
elif judgment == "perfect":
    print(int(lv)*1000)
