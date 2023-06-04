import sys; sys.stdin = open("14215.txt", "r")

arr = list(map(int, input().split()))
new = sorted(arr)

answer = new[0] + new[1] + min(new[2], (new[0]+new[1]-1))
print(answer)
