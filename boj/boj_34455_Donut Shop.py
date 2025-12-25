d = int(input())
e = int(input())

for i in range(e):
    a = input()
    q = int(input())
    if a == "+":
        d += q
    elif a == "-":
        d -= q
print(d)