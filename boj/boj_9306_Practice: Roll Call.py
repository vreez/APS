import sys; sys.stdin = open("9306.txt", "r")

N = int(input())
for i in range(N):
    first = input()
    last = input()
    print("Case {}: {}, {}".format(i+1, last, first))