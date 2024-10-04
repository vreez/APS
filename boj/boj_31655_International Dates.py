import sys; sys.stdin = open("31655.txt", "r")

dates = list(map(int, input().split("/")))
if dates[0] > 12:
    print("EU")
elif dates[1] > 12:
    print("US")
else:
    print("either")
