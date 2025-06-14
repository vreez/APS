arr = []
while True:
    num = int(input())
    if num == -1:
        break
    else:
        arr.append(num)
if len(arr) >= 3:
    for i in range(3):
        print(arr[-3:][i], end=" ")
else:
    for i in range(len(arr)):
        print(arr[i], end=" ")