import sys; sys.stdin = open("2711.txt", "r")

N = int(input())
for i in range(N):
    num, word = input().split()
    new = word[:int(num)-1] + word[int(num):]
    print(new)