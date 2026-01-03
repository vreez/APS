N = int(input())
arr = list(map(int, input().split()))

flag = True
for i in range(1, N):
    if arr[i-1] >= arr[i]:
        flag = False

if flag == True:
    print(1)
else:
    print(0)
