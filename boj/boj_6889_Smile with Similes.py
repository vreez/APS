import sys; sys.stdin = open("6889.txt", "r")

n = int(input())
m = int(input())
adj = []
nouns = []
for i in range(n):
    a = input()
    adj.append(a)
for j in range(m):
    no = input()
    nouns.append(no)

for i in range(n):
    for j in range(m):
        print("{} as {}".format(adj[i], nouns[j]))