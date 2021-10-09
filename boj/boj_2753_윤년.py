import sys; sys.stdin = open("2753.txt", "r")

answer = 0
N = input()
if (len(N) > 2 and N[-3:0] == '00') or int(N) % 4 == 0:
    if int(N) % 100 != 0 or int(N) % 400 == 0:
        answer = 1
print(answer)