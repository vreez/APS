import sys; sys.stdin = open("6438.txt", "r")

N = int(input())
for i in range(N):
    arr = list(input().split())
    new = arr[::-1]
    for j in range(len(new)):
        word = new[j][::-1]
        print(word, end=" ")
    print()
