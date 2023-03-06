import sys; sys.stdin = open("5949.txt", "r")

num = list(input())[::-1]
answer = ''
for i in range(len(num)):
    if i < len(num) and i != 0:
        if i % 3 == 0:
            answer += ','
    answer += num[i]

print(answer[::-1])

