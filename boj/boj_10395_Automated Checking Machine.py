import sys; sys.stdin = open("10395.txt", "r")

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

flag = True
for i in range(5):
    if arr1[i] + arr2[i] != 1:
        flag = False
if flag == True:
    print("Y")
else:
    print("N")