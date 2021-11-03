import sys; sys.stdin = open("1658.txt", "r")

N, M = map(int, input().split())

def big(N, M):
    while M:
        N, M = M, N % M
    return N

print(big(N, M))

def small(N, M):
    result = (N * M) // big(N, M)
    return result

print(small(N, M))
