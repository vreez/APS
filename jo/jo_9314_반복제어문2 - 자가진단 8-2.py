N = int(input())

cnt = 0
for i in range(1, 10):
    print("{} * {} = {}".format(N, i, N * i), end="   ")
    cnt += 1
    if cnt == 3:
        cnt = 0
        print()
