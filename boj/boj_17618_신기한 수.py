import sys; sys.stdin = open("17618.txt", "r")

N = int(input())

if N < 10:
    cnt = N
else:
    cnt = 0
    for i in range(1, N+1):
        if i < 10:
            cnt += 1
        else:
            num = str(i)
            check = 0
            for j in range(len(num)):
                check += int(num[j])

            if i % check == 0:
                cnt += 1

print(cnt)