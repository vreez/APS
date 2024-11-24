import sys; sys.stdin = open("9585.txt", "r")

arr = []
for _ in range(5):
    word = input()
    arr.append(word)

for i in range(5):
    print(arr[i])
