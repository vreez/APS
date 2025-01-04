import sys; sys.stdin = open("9532.txt", "r")

li = []
for i in range(3):
    print("문자열을 입력하시오:", end=" ")
    li.append(input())

print(li)