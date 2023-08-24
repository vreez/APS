import sys; sys.stdin = open("20299.txt", "r")

N, K, L = map(int, input().split())
arr = []
count = 0
for i in range(N):
    x1, x2, x3 = map(int, input().split())
    if x1 >= L and x2 >= L and x3 >= L and x1+x2+x3 >= K:
        count += 1
        arr.append(x1)
        arr.append(x2)
        arr.append(x3)
print(count)
for i in range(len(arr)):
    print(arr[i], end=" ")
