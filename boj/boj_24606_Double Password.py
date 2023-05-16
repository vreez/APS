import sys; sys.stdin = open("24606.txt", "r")

first = list(input())
second = list(input())

cnt = 0
for i in range(4):
    if first[i] != second[i]:
        cnt += 1
print(2**cnt)