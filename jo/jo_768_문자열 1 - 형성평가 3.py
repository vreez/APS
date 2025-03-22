import sys; sys.stdin = open("768.txt", "r")

one = input()
two = input()
three = input()
four = input()

first = "%s:"%one
second = "%s"%two
third = "%s:"%three
fourth = "%s"%four

print(first, second)
print(third, fourth)