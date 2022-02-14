import sys; sys.stdin = open("12813.txt", "r")

A = list(input())
B = list(input())

one = ""
two = ""
three = ""
four = ""
five = ""

for i in range(len(A)):
    if A[i] == B[i]:
        one += A[i]
    else:
        one += "0"
for i in range(len(A)):
    if A[i] == B[i]:
        two += A[i]
    else:
        two += "1"
for i in range(len(A)):
    if A[i] == B[i]:
        three += "0"
    else:
        three += "1"

for i in range(len(A)):
    if A[i] == "0":
        four += "1"
    else:
        four += "0"

for i in range(len(B)):
    if B[i] == "0":
        five += "1"
    else:
        five += "0"

print(one)
print(two)
print(three)
print(four)
print(five)