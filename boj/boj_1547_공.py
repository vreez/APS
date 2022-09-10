import sys; sys.stdin = open("1547.txt", "r")

N = int(input())
answer = [1, 0, 0]
for i in range(N):
    a, b = map(int, input().split())
    temp = answer[a-1]
    answer[a-1] = answer[b-1]
    answer[b-1] = temp

for i in range(3):
    if answer[i] == 1:
        print(i+1)