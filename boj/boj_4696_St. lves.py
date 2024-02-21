import sys; sys.stdin = open("4696.txt", "r")

while True:
    n = float(input())
    if n == 0:
        break
    else:
        ans = round((n**0 + n**1 + n**2 + n**3 + n**4), 2)
        print(f"{ans:.2f}")
