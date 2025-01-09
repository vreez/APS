import sys; sys.stdin = open("922.txt", "r")

arr = list(input().split())
li = [0] * 26
for i in range(len(arr)):
    li[ord(arr[i])-65] += 1

for i in range(len(li)):
    if li[i] != 0:
        print("{} : {}".format(chr(i+65), li[i]))

