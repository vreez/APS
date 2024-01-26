import sys; sys.stdin = open("7947.txt", "r")

n = int(input())
for i in range(n):
    totalA, totalB, totalC = 0, 0, 0
    for j in range(10):
        a, b, c = map(int, input().split())
        totalA += a
        totalB += b
        totalC += c
    midA = totalA / 10
    midB = totalB / 10
    midC = totalC / 10
    if midA % 1 == 0.5:
        midA += 0.1
    if midB % 1 == 0.5:
        midB += 0.1
    if midC % 1 == 0.5:
        midC += 0.1

    ansA = round(midA)
    ansB = round(midB)
    ansC = round(midC)
    print(ansA, ansB, ansC)