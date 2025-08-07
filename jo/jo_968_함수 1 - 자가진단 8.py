a, b = map(int, input().split())

def func(m, n):
    if m < n:
        for i in range(m, n+1):
            print("== {}dan ==".format(i))
            for j in range(1, 10):
                if i * j < 10:
                    print("{} * {} =  {}".format(i, j, i*j))
                else:
                    print("{} * {} = {}".format(i, j, i*j))
            print()
    else:
        for i in range(n, m+1):
            print("== {}dan ==".format(i))
            for j in range(1, 10):
                if i * j < 10:
                    print("{} * {} =  {}".format(i, j, i*j))
                else:
                    print("{} * {} = {}".format(i, j, i*j))
            print()

func(a, b)