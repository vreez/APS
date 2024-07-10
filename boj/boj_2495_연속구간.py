import sys; sys.stdin = open("2495.txt", "r")

for i in range(3):
    arr = list(input())
    ans = 1
    res = []
    for j in range(1, 8):
        if arr[j-1] == arr[j]:
            ans += 1
        else:
            res.append(ans)
            ans = 1
    res.append(ans)
    print(max(res))
