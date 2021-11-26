import sys; sys.stdin = open("1357.txt", "r")

X, Y = input().split()
X = list(reversed(X))
Y = list(reversed(Y))

num1 = int(''.join(X))
num2 = int(''.join(Y))

total = list(reversed(str(num1 + num2)))

result = int(''.join(total))

print(result)