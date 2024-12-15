import sys; sys.stdin = open("9514.txt", "r")

first = int(input())
second = int(input())

print("수를 입력하시오.", end=" ")
print("수를 입력하시오.", end=" ")
print("{} + {} = {}".format(first, second, first + second))
print("{} - {} = {}".format(first, second, first - second))
print("{} * {} = {}".format(first, second, first * second))
print("{} // {} = {}".format(first, second, first // second))
print("{} % {} = {}".format(first, second, first % second))
print("{} ** {} = {}".format(first, second, first ** second))