import sys; sys.stdin = open("6249.txt", "r")

n, p, h = map(int, input().split())
for i in range(n):
    rec = int(input())
    if rec < p:
        print("NTV: Dollar dropped by {} Oshloobs".format(p-rec))
    elif rec > h:
        print("BBTV: Dollar reached {} Oshloobs, A record!".format(rec))
        h = rec
    p = rec