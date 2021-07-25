import sys; sys.stdin = open("input/2675.txt", "r")

T = int(input())
arr = [list(input().split()) for _ in range(T)]

for i in range(T):
    word = ''
    for j in range(len(arr[i][1])):
        word += (arr[i][1][j] * int(arr[i][0]))
    print(word)
