import sys; sys.stdin = open("23809.txt", "r")

N = int(input())
for i in range(5*N):
    if i//N == 0 or i//N == 4:
        print("@"*N+" "*N*3+"@"*N)
    elif i//N == 2:
        print("@"*N*3)
    else:
        print("@"*N+" "*N*2+"@"*N)