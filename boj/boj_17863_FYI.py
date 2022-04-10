import sys; sys.stdin = open("17863.txt", "r")

num = input()
if len(num) == 7 and num[:3] == "555":
    print("YES")
else:
    print("NO")
