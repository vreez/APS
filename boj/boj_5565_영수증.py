import sys; sys.stdin = open("input/5565.txt", "r")

total = int(input())
books = 0
for _ in range(9):
    books += int(input())
print(total - books)