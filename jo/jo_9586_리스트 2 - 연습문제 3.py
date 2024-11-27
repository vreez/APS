import sys; sys.stdin = open("9586.txt", "r")

arr = ["champion", "tel", "pencil", "jungol", "olympiad", "class", "information", "lesson", "book", "lion"]
ch = input()

cnt = 0
check = []
for i in range(len(arr)):
    if arr[i][0] == ch:
        cnt += 1
        check.append(arr[i])
if cnt > 0:
    print("문자를 입력하세요.", end=" ")
    for i in range(len(check)):
        print(check[i])
else:
    print("찾는 단어가 없습니다.")

