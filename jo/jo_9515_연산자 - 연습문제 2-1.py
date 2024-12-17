import sys; sys.stdin = open("9515.txt", "r")

print("정수를 입력하시오.", end=" ")
print("정수를 입력하시오.", end=" ")
print("정수를 입력하시오.", end=" ")
print("정수를 입력하시오.", end=" ")
print("정수를 입력하시오.", end=" ")
print("정수를 입력하시오.", end=" ")

for i in range(6):
    num = int(input())
    if i == 0:
        print(num + 3, end=" ")
    elif i == 1:
        print(num - 3, end=" ")
    elif i == 2:
        print(num * 3, end=" ")
    elif i == 3:
        print(num // 3, end=" ")
    elif i == 4:
        print(num % 3, end=" ")
    else:
        print(num ** 3, end=" ")

