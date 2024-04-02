import sys; sys.stdin = open("19774.txt", "r")

B = int(input())
for i in range(B):
    num = input()
    one = num[:2]
    two = num[2:]
    if (int(one)**2 + int(two)**2)%7 == 1:
        print("YES")
    else:
        print("NO")