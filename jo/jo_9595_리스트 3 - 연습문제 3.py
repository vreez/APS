import sys; sys.stdin = open("9595.txt", "r")

arr = list(map(int, input().split()))
li = [0] * 10
for i in range(len(arr)):
    li[arr[i] % 10] += 1

for i in range(len(li)):
    if li[i] != 0:
        print("{} : {}개".format(i, li[i]))
