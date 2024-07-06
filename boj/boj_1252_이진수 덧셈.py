import sys; sys.stdin = open("1252.txt", "r")

first, second = input().split()
n_first = int(first, 2)
n_second = int(second, 2)
ans = n_first + n_second
print(bin(ans)[2:])