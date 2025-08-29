import sys; sys.stdin = open("943.txt", "r")
n = int(input())
tp = ()
for i in range(n):
    tp += tuple(input().split())

for i in range(3*n):
    if tp[i] == "Platinum":
        print("[Gosu] {}".format(tp[i-2]))
    elif tp[i] == "Silver" or tp[i] == "Gold":
        if float(tp[i-1]) >= 60.0:
            print("[Gosu] {}".format(tp[i-2]))
