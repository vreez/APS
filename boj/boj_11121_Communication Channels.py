import sys; sys.stdin = open("11121.txt", "r")

N = int(input())
for i in range(N):
    A, B = input().split()
    flag = True
    for j in range(len(A)):
        if A[j] != B[j]:
            flag = False
            break
    if flag == False:
        print("ERROR")
    else:
        print("OK")