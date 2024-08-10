import sys; sys.stdin = open("27326.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
li = []
for i in range(1, N+1):
    for _ in range(2):
        li.append(i)

for j in range(N*2-1):
    li.remove(arr[j])

print(li[0])


