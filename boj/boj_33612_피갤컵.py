import sys; sys.stdin = open("33612.txt", "r")
n = int(input())

if n == 1:
    print("{} {}".format(2024, 8))
elif n == 2:
    print("{} {}".format(2025, 3))
elif n == 3:
    print("{} {}".format(2025, 10))
elif n == 4:
    print("{} {}".format(2026, 5))
else:
    print("{} {}".format(2026, 12))
