import sys; sys.stdin = open("7241.txt", "r")
import itertools

arr = list(input().split())
num = int(input())
ans = []
li = itertools.permutations(arr, 3)
new = list(li)
for i in range(len(new)):
    ans.append(int("".join(new[i])))
ans = sorted(ans)
print(ans.index(num)+1)