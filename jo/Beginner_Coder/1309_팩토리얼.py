import sys; sys.stdin = open("1309.txt", "r")

N = int(input())
answer = 1
while N > 1:
    print("{}! = {} * {}!".format(N, N, N-1))
    answer *= N
    N -= 1
print("1! = 1")
print(answer)

