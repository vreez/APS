import sys; sys.stdin = open("20499.txt", "r")

K, D, A = map(int, input().split('/'))

if K + A < D or D == 0:
    print("hasu")
else:
    print("gosu")