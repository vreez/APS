import sys; sys.stdin = open("25840.txt", "r")

N = int(input())
arr = []
for i in range(N):
    bday = input()
    if bday not in arr:
        arr.append(bday)

print(len(arr))