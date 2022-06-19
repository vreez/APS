import sys; sys.stdin = open("18409.txt", "r")
vowels = ["a", "i", "u", "e", "o"]

N = int(input())
S = list(input())

count = 0
for i in range(N):
    if S[i] in vowels:
        count += 1

print(count)