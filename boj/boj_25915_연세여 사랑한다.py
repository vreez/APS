import sys; sys.stdin = open("25915.txt", "r")

N = input()
num = ord(N) - 65
ans = abs(num - 8) + 84
print(ans)