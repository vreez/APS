import sys; sys.stdin = open("26546.txt", "r")

N = int(input())
for i in range(N):
    word, a, b = input().split()
    answer1 = word[0:int(a)]
    answer2 = word[int(b):]
    print(answer1+answer2)
    