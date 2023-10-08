import sys; sys.stdin = open("30214.txt", "r")

s1, s2 = map(int, input().split())
if (s2 / 2) <= s1:
    print("E")
else:
    print("H")