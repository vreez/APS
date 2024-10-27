import sys; sys.stdin = open("5349.txt", "r")

arr = list(input().split())
new = []
for i in range(len(arr)):
    if i % 2 != 0:
        new.append(arr[i])

for word in new[::-1]:
    print(word, end=" ")

