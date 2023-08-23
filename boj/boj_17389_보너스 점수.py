import sys; sys.stdin = open("17389.txt", "r")

N = int(input())
arr = list(input())
total = 0
score = 0
bonus = 0
for i in range(len(arr)):
    if arr[i] == "X":
        bonus = 0
    else:
        score = i+1
        total += (score+bonus)
        bonus += 1
print(total)
