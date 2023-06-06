import sys; sys.stdin = open("28114.txt", "r")

first = []
second = []
for i in range(3):
    P, Y, S = input().split()
    first.append(int(Y) % 100)
    second.append([int(P), S[0]])

first = sorted(first)
second = sorted(second, reverse=True)
new = second[0][1] + second[1][1] + second[2][1]

print(first[0]*10000 + first[1]*100 + first[2])
print(new)
