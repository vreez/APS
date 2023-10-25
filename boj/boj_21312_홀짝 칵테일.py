import sys; sys.stdin = open("21312.txt", "r")

arr = list(map(int, input().split()))

odd = []
even = []
for i in range(3):
    if arr[i] % 2:
        odd.append(arr[i])
    else:
        even.append(arr[i])

if len(odd) > 0:
    ans = 1
    for j in range(len(odd)):
        ans *= odd[j]
else:
    ans = 1
    for j in range(len(even)):
        ans *= even[j]

print(ans)