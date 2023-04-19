import sys; sys.stdin = open("20053.txt", "r")

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(min(arr), max(arr))
