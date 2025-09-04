n = int(input())

for i in range(n):
    print(" "*((2*n-1)-(2*(i+1)-1)), end="")
    for j in range(1, i+2):
        print(j, end=" ")
    print()
