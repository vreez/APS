import sys; sys.stdin = open("30468.txt", "r")

str, dex, int, luk, n = map(int, input().split())

avg = (str + dex + int + luk) // 4
if avg >= n:
    print(0)
else:
    ans = (n * 4) - (str + dex + int + luk)
    print(ans)