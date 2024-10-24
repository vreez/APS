import sys; sys.stdin = open("1056.txt", "r")

n, m = map(int, input().split())
cnt = 0
for i in range(n, m+1):
    check = i % 10
    if check != 0 and check % 3 == 0:
        cnt += 1
        print(i)
print(cnt)
