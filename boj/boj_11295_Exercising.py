import sys; sys.stdin = open("11295.txt", "r")
cnt = 0
while True:
    N = int(input())
    cnt += 1
    if N == 0:
        break
    else:
        print("User {}".format(cnt))
        M = int(input())
        for i in range(M):
            num = int(input())
            ans = N * num * 0.00001
            print("{:.5f}".format(ans))
