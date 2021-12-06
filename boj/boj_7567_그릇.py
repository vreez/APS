import sys; sys.stdin = open("7567.txt", "r")

dish = list(input())

answer = 10
for i in range(1, len(dish)):
    if dish[i] != dish[i-1]:
        answer += 10
    else:
        answer += 5

print(answer)