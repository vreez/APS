import sys; sys.stdin = open("2514.txt", "r")

N = input()
koiCount = 0
ioiCount = 0
for i in range(0, len(N)-2):
    if N[i:i+3] == "KOI":
        koiCount += 1
    elif N[i:i+3] == "IOI":
        ioiCount += 1

print(koiCount)
print(ioiCount)