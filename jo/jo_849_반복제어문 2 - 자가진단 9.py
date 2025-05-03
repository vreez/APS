for i in range(3):
    for j in range(5):
        if (i+2)*(j+1) >= 10:
            print("{} * {} = {}".format(i+2, j+1, ((i+2)*(j+1))),end="   ")
        else:
            print("{} * {} =  {}".format(i+2, j+1, ((i+2)*(j+1))),end="   ")
    print()