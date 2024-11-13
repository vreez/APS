import sys; sys.stdin = open("9018.txt", "r")

a, b = map(int, input().split())
print("두 개의 수를 입력하시오.", end=" ")
print("{} + {} = {}".format(a, b, a+b))
print("{} - {} = {}".format(a, b, a-b))
print("{} * {} = {}".format(a, b, a*b))
print("{} / {} = {}".format(a, b, a//b))
print("{} % {} = {}".format(a, b, a%b))