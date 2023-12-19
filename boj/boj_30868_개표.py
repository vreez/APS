import sys; sys.stdin = open("30868.txt","r")

T = int(input())
for i in range(T):
    n = int(input())
    a = n // 5
    b = n % 5
    for j in range(a):
        print("++++", end=" ")
    print("|"*b, end="")
    print()