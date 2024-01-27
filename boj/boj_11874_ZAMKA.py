import sys; sys.stdin = open("11874.txt", "r")

L = int(input())
D = int(input())
X = int(input())

arr = []
for i in range(L, D+1):
    new = [int(i) for i in str(i)]
    if sum(new) == X:
        arr.append(i)
print(arr[0])
print(arr[-1])