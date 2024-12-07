import sys; sys.stdin = open("9579.txt", "r")
first = input()
second = input()

li = [first, second]
new = sorted(li)
print(new[1])