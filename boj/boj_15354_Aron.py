import sys; sys.stdin = open("15354.txt", "r")

N = int(input())
arr = []
for i in range(N):
    al = input()
    if len(arr) == 0 or arr[-1] != al:
        arr.append(al)
print(len(arr)+1)
