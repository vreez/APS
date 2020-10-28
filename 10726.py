import sys; sys.stdin = open("10726.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    num = bin(M)[2:]

    if N <= len(num):
        cnt = 0
        for i in range(len(num)-1, len(num)-N-1, -1):
            if num[i] == '0':
                print("#{} {}".format(tc, 'OFF'))
                break
            else:
                cnt += 1
        if cnt == N:
            print("#{} {}".format(tc, 'ON'))
    else:
        print("#{} {}".format(tc, 'OFF'))

