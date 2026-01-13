first = list(map(int, input().split()))
second = list(map(int, input().split()))

arr = []
for i in range(len(first)):
    if first[i] not in second and first[i] not in arr:
        arr.append(first[i])
new = sorted(arr)

for i in range(len(new)):
    print(new[i], end=" ")
