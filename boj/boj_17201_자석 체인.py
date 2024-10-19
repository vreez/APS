import sys; sys.stdin = open("17201.txt", "r")

N = int(input())
a = list(map(int, input()))
flag = True
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")