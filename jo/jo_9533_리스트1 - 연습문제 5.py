import sys; sys.stdin = open("9533.txt", "r")

words = list(input().split())
new = list(words[-1])
print("String?", new)
print(new[2])