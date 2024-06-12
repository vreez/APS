import sys; sys.stdin = open("16316.txt", "r")

n = int(input())
arr = list(input().split())
flag = True
for i in range(1, len(arr)+1):
    if arr[i-1] != "mumble":
        if int(arr[i-1]) == i:
            continue
        else:
            flag = False
            break
if flag:
    print("makes sense")
else:
    print("something is fishy")
