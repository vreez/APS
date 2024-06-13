import sys; sys.stdin = open("1233.txt", "r")

s1, s2, s3 = map(int, input().split())
arr = [0] * (s1+s2+s3+1)
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            arr[i+j+k] += 1

for i in range(len(arr)):
    if max(arr) == arr[i]:
        print(i)
        break