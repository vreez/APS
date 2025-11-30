N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

if arr[0] == min(arr):
    print("ez")
elif arr[0] == max(arr):
    print("hard")
else:
    print("?")
