import sys; sys.stdin = open("26592.txt", "r")

N = int(input())
for i in range(N):
    a, b = map(float, input().split())
    answer = round((a*2)/b, 2)
    print("The height of the triangle is {:.2f} units".format(answer))
