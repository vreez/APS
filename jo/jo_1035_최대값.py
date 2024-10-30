import sys; sys.stdin = open("1035.txt", "r")

arr = []
for _ in range(9):
    num = int(input())
    arr.append(num)

mx = max(arr)
ans = arr.index(mx)
print(mx)
print(ans+1)