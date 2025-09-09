import sys; sys.stdin = open("9598.txt")

first = [list(input().split()) for _ in range(3)]
second = [list(input().split()) for _ in range(3)]


print("첫 번째 배열 1행 첫 번째 배열 2행 첫 번째 배열 3행 두 번째 배열 1행 두 번째 배열 2행 두 번째 배열 3행", end=" ")
for i in range(3):
    for j in range(3):
        print(int(first[i][j]) + int(second[i][j]), end=" ")
    print()
