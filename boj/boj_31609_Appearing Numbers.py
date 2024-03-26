import sys; sys.stdin = open("31609.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
new = sorted(list(set(arr)))

for i in range(len(new)):
    print(new[i])
