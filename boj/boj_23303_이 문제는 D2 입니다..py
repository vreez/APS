import sys; sys.stdin = open("23303.txt", "r")

arr = input()

flag = False
if "d2" in arr:
    flag = True
elif "D2" in arr:
    flag = True

if flag == True:
    print("D2")
else:
    print("unrated")