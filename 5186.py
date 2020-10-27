import sys; sys.stdin = open("5186.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    k = 1
    arr = []
    while N % (2 ** -k) != 0:
        if N // (2 ** -k) == 1:
            arr.append('1')
            N = N % (2 ** -k)
        elif N // (2 ** -k) == 0:
            arr.append('0')
        k += 1
    arr.append('1')

    if len(arr) >= 13:
        print("#{} {}".format(tc, 'overflow'))
    else:
        print("#{} {}".format(tc, ''.join(arr)))


