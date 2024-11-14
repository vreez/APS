import sys; sys.stdin = open("9019.txt", "r")

arr = list(map(int, input().split()))
print("5개의 수를 입력하시오.", end=" ")
for i in range(5):
    if i == 0:
        print(arr[i] + 3, end=" ")
    elif i == 1:
        print(arr[i] - 3, end=" ")
    elif i == 2:
        print(arr[i] *3, end=" ")
    elif i == 3:
        print(arr[i] //3, end=" ")
    else:
        print(arr[i] % 3, end=" ")