import sys; sys.stdin = open("11006.txt", "r")

T = int(input())
for i in range(T):
    U, T = map(int, input().split())
    print((T * 2) - U, T - ((T * 2) - U))