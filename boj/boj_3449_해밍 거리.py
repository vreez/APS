import sys; sys.stdin = open("3449.txt", "r")

T = int(input())
for i in range(T):
    ans = 0
    a = list(input())
    b = list(input())
    for j in range(len(a)):
        if a[j] != b[j]:
            ans += 1
    print("Hamming distance is {}.".format(ans))