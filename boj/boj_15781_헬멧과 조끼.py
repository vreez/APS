import sys; sys.stdin = open("15781.txt", "r")

N, M = map(int, input().split())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

print(max(h)+max(a))