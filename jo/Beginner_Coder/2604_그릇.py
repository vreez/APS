import sys; sys.stdin = open("2604.txt", "r")

dish = list(input())

height = 10
for i in range(len(dish)-1):
    if dish[i] != dish[i+1]:
        height += 10
    else:
        height += 5

print(height)