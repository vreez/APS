import sys; sys.stdin = open("17249.txt", "r")

arr = list(input().split("(^0^)"))
one = arr[0].count("@")
two = arr[1].count("@")

print(one, two)
