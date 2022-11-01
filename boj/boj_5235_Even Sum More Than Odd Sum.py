import sys; sys.stdin = open("5235.txt", "r")

N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    k = arr[0]
    new = arr[1:]
    even = 0
    odd = 0
    for j in range(k):
        if new[j] % 2:
            odd += new[j]
        else:
            even += new[j]
    if odd > even:
        print("ODD")
    elif even > odd:
        print("EVEN")
    else:
        print("TIE")