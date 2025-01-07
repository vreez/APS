import sys; sys.stdin = open("9593.txt", "r")

arr = list(map(int, input().split()))
new = sorted(arr)
li = [0] * 11
for i in range(len(arr)):
    li[arr[i]] += 1

for i in range(11):
    if li[i] != 0:
        print("{} : {}개".format(i, li[i]))



