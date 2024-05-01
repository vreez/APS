import sys; sys.stdin = open("31775.txt")

s1 = input()
s2 = input()
s3 = input()

li = [s1[0], s2[0], s3[0]]
if 'l' in li and 'k' in li and 'p' in li:
    print("GLOBAL")
else:
    print("PONIX")