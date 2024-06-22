import sys; sys.stdin = open("1978.txt", "r")
import math;

N = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(N):
    if arr[i] != 1:
        check = True
        for j in range(2, int(math.sqrt(arr[i])+1)):
            if arr[i] % j == 0:
                check = False
                break
        if check == True:
            ans += 1
print(ans)