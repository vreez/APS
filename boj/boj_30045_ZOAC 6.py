import sys; sys.stdin = open("30045.txt", "r")

N = int(input())
total = 0
for i in range(N):
    word = input()
    if "01" in word or "OI" in word:
        total += 1

print(total)