import sys; sys.stdin = open("1427.txt", "r")

number = list(map(int, input()))
number = sorted(number, reverse=True)
for i in range(len(number)):
    print(number[i], end='')

