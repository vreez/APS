import sys; sys.stdin = open("30596.txt", "r")

arr = []
for i in range(4):
    N = int(input())
    arr.append(N)
new = sorted(arr)

print(new[0] * new[2])