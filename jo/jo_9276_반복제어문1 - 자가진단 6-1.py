while True:
    num = int(input())
    if num < 0 or num > 100:
        break
    else:
        print("Score: {}".format(num))