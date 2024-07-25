import sys; sys.stdin = open("16503.txt", "r")

n1, a, n2, b, n3 = input().split()
first = 0
if a == "+":
    first = int(n1) + int(n2)
elif a == "-":
    first = int(n1) - int(n2)
elif a == "*":
    first = int(n1) * int(n2)
elif a == "/":
    if int(n1) * int(n2) < 0:
        first = -1 * (abs(int(n1)) // abs(int(n2)))
    else:
        first = int(n1)//int(n2)
if b == "+":
    first += int(n3)
elif b == "-":
    first -= int(n3)
elif b == "*":
    first *= int(n3)
elif b == "/":
    if first * int(n3) < 0:
        first = -1 * (abs(first) // abs(int(n3)))
    else:
        first = first // int(n3)

second = 0
if b == "+":
    second = int(n2) + int(n3)
elif b == "-":
    second = int(n2) - int(n3)
elif b == "*":
    second = int(n2) * int(n3)
elif b == "/":
    if int(n2) * int(n3) < 0:
        second = -1 * (abs(int(n2)) // abs(int(n3)))
    else:
        second = int(n2) // int(n3)
if a == "+":
    second = int(n1) + second
elif a == "-":
    second = int(n1) - second
elif a == "*":
    second = int(n1) * second
elif a == "/":
    if  second * int(n1) < 0:
        second = -1 * (abs(int(n1)) // abs(second))
    else:
        second = int(n1) // second

res = [int(first), int(second)]
print(min(res))
print(max(res))


