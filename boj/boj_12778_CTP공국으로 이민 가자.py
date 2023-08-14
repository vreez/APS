import sys; sys.stdin = open("12778.txt", "r")

N = int(input())
for i in range(N):
    num, type = input().split()
    arr = list(input().split())
    if type == "C":
        for j in range(int(num)):
            print(ord(arr[j])-64, end=" ")
    else:
        for j in range(int(num)):
            print(chr(int(arr[j])+64), end=" ")
    print()

