import sys; sys.stdin = open("1439.txt", "r")

N = list(input())

arr = [N[0]]
for i in range(1, len(N)):
    if N[i] != arr[-1]:
        arr.append(N[i])

zero = 0
one = 0
for i in range(len(arr)):
    if arr[i] == '0':
        zero += 1
    else:
        one += 1

print(min(zero, one))