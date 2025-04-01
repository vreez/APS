while True:
    print("number?", end=" ")
    N = int(input())
    if N == 0:
        break
    else:
        if N > 0 :
            print("positive integer")
        else:
            print("negative number")

