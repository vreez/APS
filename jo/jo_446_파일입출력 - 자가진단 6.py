while True:
    num = float(input())
    if num == 0 :
        break
    else:
        ans = num / (3.14 * 2)
        print("{:.2f}".format(ans))