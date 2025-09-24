arr = list(map(int, input().split()))

for i in range(1, 7):
    print("{} : {}".format(i, arr.count(i)))
