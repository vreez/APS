import sys; sys.stdin = open("6190.txt", "r")

N = int(input())

answer = 0
while True:
    if N == 1:
        break
    else:
        if N % 2:
            N = (N*3)+1
        else:
            N = (N//2)
        answer += 1

print(answer)

