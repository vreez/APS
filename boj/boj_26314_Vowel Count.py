import sys; sys.stdin = open("26314.txt", "r")

vowels = ["a", "e", "i", "o", "u"]
N = int(input())
for i in range(N):
    name = list(input())
    v = 0
    c = 0
    for j in range(len(name)):
        if name[j] in vowels:
            v += 1
        else:
            c += 1
    if v > c:
        print("".join(name))
        print(1)
    else:
        print("".join(name))
        print(0)
