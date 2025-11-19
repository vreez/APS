N = int(input())

arr = list(map(int, input().split()))
ang = 0
ans = 0
for i in range(N):
    if arr[i] == 1:
        ang += 1
        ans += ang
    else:
        ang -= 1
        ans += ang
print(ans)