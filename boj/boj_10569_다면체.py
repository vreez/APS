import sys; sys.stdin = open("10569.txt", "r")

T = int(input())
for i in range(T):
    V, E = map(int, input().split())
    result = 2 - V + E
    print(result)
