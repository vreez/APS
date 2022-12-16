import sys; sys.stdin = open("26209.txt", "r")

arr = list(map(int, input().split()))
flag = True
for i in range(8):
    if arr[i] != 1 and arr[i] != 0:
        flag = False
        break

if flag == True:
    print("S")
else:
    print("F")