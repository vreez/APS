import sys; sys.stdin = open("1098.txt", "r")

num = list(input())
total = 0
for i in range(len(num)):
    if num[i] == "0":
        total += 6
    elif num[i] == "1":
        total += 2
    elif num[i] == "2":
        total += 5
    elif num[i] == "3":
        total += 5
    elif num[i] == "4":
        total += 4
    elif num[i] == "5":
        total += 5
    elif num[i] == "6":
        total += 6
    elif num[i] == "7":
        total += 3
    elif num[i] == "8":
        total += 7
    elif num[i] == "9":
        total += 6

print(total)

