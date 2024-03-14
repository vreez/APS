import sys; sys.stdin = open("31518.txt", "r")

N = int(input())
check = 0
for i in range(3):
    arr = list(map(int, input().split()))
    if 7 in arr:
        check += 1
if check == 3:
    print(777)
else:
    print(0)
