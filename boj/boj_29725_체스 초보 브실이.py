import sys; sys.stdin = open("29725.txt", "r")

w = 0
b = 0
for i in range(8):
    arr = list(input())
    for j in range(8):
        if arr[j] == "P":
            w += 1
        elif arr[j] == "p":
            b += 1
        elif arr[j] == "N" or arr[j] == "B":
            w += 3
        elif arr[j] == "n" or arr[j] == "b":
            b += 3
        elif arr[j] == "R":
            w += 5
        elif arr[j] == "r":
            b += 5
        elif arr[j] == "Q":
            w += 9
        elif arr[j] == "q":
            b += 9

print(w-b)