import sys; sys.stdin = open("756.txt", "r")

one = input()
two = input()
three = int(input())

for i in range(three):
    print(two, end="")
print(one)
