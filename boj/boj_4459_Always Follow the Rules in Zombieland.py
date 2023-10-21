import sys; sys.stdin = open("4459.txt", "r")

arr = []
N = int(input())
for i in range(N):
    arr.append(input())
M = int(input())
for j in range(M):
    num = int(input())
    if num <= 0 or num > N:
        print("Rule {}: No such rule".format(num))
    else:
        print("Rule {}: {}".format(num, arr[num-1]))