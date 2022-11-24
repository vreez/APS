import sys; sys.stdin = open("11367.txt", "r")

N = int(input())
for i in range(N):
    name, num = list(input().split())
    if int(num) >= 97 and int(num) <= 100:
        print(name, "A+")
    elif int(num) >= 90 and int(num) <= 96:
        print(name, "A")
    elif int(num) >= 87 and int(num) <= 89:
        print(name, "B+")
    elif int(num) >= 80 and int(num) <= 86:
        print(name, "B")
    elif int(num) >= 77 and int(num) <= 79:
        print(name, "C+")
    elif int(num) >= 70 and int(num) <= 76:
        print(name, "C")
    elif int(num) >= 67 and int(num) <= 69:
        print(name, "D+")
    elif int(num) >= 60 and int(num) <= 66:
        print(name, "D")
    else:
        print(name, "F")
