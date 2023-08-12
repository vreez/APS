import sys; sys.stdin = open("3028.txt", "r")

cup = [1, 0, 0]
arr = list(input())
for i in range(len(arr)):
    if arr[i] == "A":
        imsi = cup[0]
        cup[0] = cup[1]
        cup[1] = imsi
    elif arr[i] == "B":
        imsi = cup[1]
        cup[1] = cup[2]
        cup[2] = imsi
    else:
        imsi = cup[0]
        cup[0] = cup[2]
        cup[2] = imsi

result = cup.index(1) + 1
print(result)