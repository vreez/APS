import sys; sys.stdin = open("10886.txt", "r")

N = int(input())
one = 0
zero = 0
for i in range(N):
    if int(input()) == 1:
        one += 1
    else:
        zero += 1

if one > zero:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")