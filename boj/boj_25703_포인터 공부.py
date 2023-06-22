import sys; sys.stdin = open("25703.txt", "r")

N = int(input())

for i in range(N):
    if i == 0:
        print("int a;")
        print("int *ptr = &a;")
    elif i == 1:
        print("int **ptr2 = &ptr;")
    else:
        print("int {}ptr{} = &ptr{};".format(("*"*(i+1)), i+1, i))