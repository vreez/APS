while True:
    N = int(input())
    if N == -1:
        break
    else:
        if N % 3 == 0:
            print(N // 3)