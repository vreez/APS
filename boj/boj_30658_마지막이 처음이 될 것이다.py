import sys; sys.stdin = open("30658.txt", "r")

while True:
    N = int(input())
    if N == 0:
        break
    else:
        arr = []
        for i in range(N):
            num = int(input())
            arr.append(num)
        new = arr[::-1]
        for j in range(N):
            print(new[j])
        print(0)
