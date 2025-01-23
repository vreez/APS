while True:
    print("number?", end=" ")
    num = int(input())
    if num == 0:
        break
    else:
        if num > 0:
            print("positive integer")
        else:
            print("negative number")