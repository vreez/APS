import sys; sys.stdin = open("8806.txt", "r")

N = int(input())
for i in range(N):
    a, b, c = map(float, input().split())
    x, y, z = map(float, input().split())
    adam = a*y + b*z + c*x
    gosia = x*b + y*c + z*a
    if adam > gosia:
        print("ADAM")
    elif gosia > adam:
        print("GOSIA")
    else:
     print("=")