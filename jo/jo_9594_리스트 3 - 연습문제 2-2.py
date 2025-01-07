import sys; sys.stdin = open("9594.txt", "r")

arr = list(map(int, input().split()))
li = [0] * 11
new = sorted(arr)
for i in range(len(new)):
    li[new[i]] += 1
for i in range(11):
    if li[i] >= 1:
        print("{} : {}개".format(i, li[i]))
