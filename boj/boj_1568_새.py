import sys; sys.stdin = open("1568.txt", "r")

N = int(input())
sec = 1
cnt = 0
while True:
    if N == 0:
        break
    else:
       if sec > N:
           sec = 1
           N -= sec
       else:
           N -= sec
       sec += 1
       cnt += 1
print(cnt)
