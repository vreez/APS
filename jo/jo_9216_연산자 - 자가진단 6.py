arr = list(map(int, input().split()))
if arr[0] == arr[1] and arr[1] == arr[2]:
    print(False)
else:
    if arr[0] == max(arr):
        print(True)
    else:
        print(False)

if arr[0] == arr[1] and arr[1] == arr[2]:
    print(True)
else:
    print(False)