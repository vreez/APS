import sys; sys.stdin = open("2455.txt", "r")

total = 0
result = 0
for i in range(4):
    out, come = map(int, input().split())
    total -= out
    total += come
    if total > result:
        result = total

print(result)