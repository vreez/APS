import sys; sys.stdin = open("11007.txt", "r")

T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    ans = ""
    for j in range(n):
        ans += alpha[arr[j]]
        temp = alpha[arr[j]]
        alpha.pop(arr[j])
        alpha.insert(0, temp)
    print(ans)