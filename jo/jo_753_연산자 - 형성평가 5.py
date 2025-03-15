import sys; sys.stdin = open("753.txt", "r")

b = int(input())
s = int(input())
print("Brother? Sister? ", end="")
if b != s:
    print(True)
else:
    print(False)
