import sys; sys.stdin = open("9516.txt", "r")

print("정수를 입력하시오.", end=" ")
print("정수를 입력하시오.", end=" ")
print("정수를 입력하시오.", end=" ")
print("정수를 입력하시오.", end=" ")
print("정수를 입력하시오.", end=" ")
print("정수를 입력하시오.", end=" ")
arr = []
for i in range(6):
    num = int(input())
    if i == 0:
        arr.append(num + 3)
    elif i == 1:
        arr.append(num - 3)
    elif i == 2:
        arr.append(num * 3)
    elif i == 3:
        arr.append(num // 3)
    elif i == 4:
        arr.append(num % 3)
    else:
        arr.append(num ** 3)
for i in range(6):
    print(arr[i], end=" ")
