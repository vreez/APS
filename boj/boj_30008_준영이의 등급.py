import sys; sys.stdin = open("30008.txt", "r")

N, K = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(K):
    rate = arr[i] * 100 // N
    if rate >= 0 and rate <= 4:
        print(1, end=" ")
    elif rate > 4 and rate <= 11:
        print(2, end=" ")
    elif rate > 11 and rate <= 23:
        print(3, end=" ")
    elif rate > 23 and rate <= 40:
        print(4, end=" ")
    elif rate > 40 and rate <= 60:
        print(5, end=" ")
    elif rate > 60 and rate <= 77:
        print(6, end=" ")
    elif rate > 77 and rate <= 89:
        print(7, end=" ")
    elif rate > 89 and rate <= 96:
        print(8, end=" ")
    elif rate > 96 and rate <= 100:
        print(9, end=" ")