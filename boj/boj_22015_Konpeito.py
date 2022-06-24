import sys; sys.stdin = open("22015.txt", "r")

candy = list(map(int, input().split()))

maxNum = max(candy)

answer = 0
for i in range(3):
    if candy[i] < maxNum:
        answer += (maxNum - candy[i])

print(answer)