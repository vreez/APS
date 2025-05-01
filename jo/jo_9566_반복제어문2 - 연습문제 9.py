for i in range(1, 10):
    for j in range(3):
        if (j+2)*i >= 10:
            print("{} * {} = {}".format(j+2, i, (j+2)*i), end="  ")
        else:
            print("{} * {} =  {}".format(j + 2, i, (j + 2) * i), end="  ")
    print()