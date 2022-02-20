import sys; sys.stdin = open("11328.txt", "r")

N = int(input())
for _ in range(N):
    A, B = input().split()
    A = sorted(list(A))
    B = sorted(list(B))

    answer = True
    if len(A) == len(B):
        for i in range(len(A)):
            if A[i] != B[i]:
                answer = False
                break
    else:
        answer = False

    if answer == True:
        print("Possible")
    else:
        print("Impossible")