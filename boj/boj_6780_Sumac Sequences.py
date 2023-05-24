import sys; sys.stdin = open("6780.txt", "r")

t1 = int(input())
t2 = int(input())
answer = 2
while True:
    num = t1 - t2
    answer += 1
    if num > t2:
        break
    else:
        t1 = t2
        t2 = num

print(answer)