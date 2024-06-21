import sys; sys.stdin = open("1668.txt", "r")

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
mx = arr[0]
new = arr[::-1]
nm = new[0]
cnt1 = 1
cnt2 = 1
for i in range(1, N):
    if arr[i] > mx and arr[i] > arr[i-1]:
        cnt1 += 1
        mx = arr[i]
for i in range(1, N):
    if new[i] > nm and new[i] > new[i-1]:
        cnt2 += 1
        nm = new[i]
print(cnt1)
print(cnt2)