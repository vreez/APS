a, b = map(int, input().split())

if a > b:
    for i in range(1, 10):
        for j in range(a, b-1, -1):
            if j*i < 10:
                print("{} * {} =  {}".format(j, i, j*i), end="   ")
            else:
                print("{} * {} = {}".format(j, i, j * i), end="   ")
        print()
else:
    for i in range(1, 10):
        for j in range(a, b+1):
            if j * i < 10:
                print("{} * {} =  {}".format(j, i, j * i), end="   ")
            else:
                print("{} * {} = {}".format(j, i, j * i), end="   ")
        print()