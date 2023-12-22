import sys; sys.stdin = open("25285.txt", "r")

T = int(input())
for i in range(T):
    h, w = map(int, input().split())
    bmi = (w /((h*0.01)**2))
    if h < 140.1:
        print(6)
    elif h >= 140.1 and h < 146:
        print(5)
    elif h >= 146 and h < 159:
        print(4)
    elif h >= 159 and h < 161:
        if bmi >= 16 and bmi < 35:
            print(3)
        else:
            print(4)
    elif h >= 161 and h < 204:
        if bmi >= 20 and bmi < 25:
            print(1)
        elif (bmi >= 18.5 and bmi < 20) or (bmi >= 25 and bmi < 30):
            print(2)
        elif (bmi >= 16 and bmi < 18.5) or (bmi >= 30 and bmi < 35):
            print(3)
        else:
            print(4)
    else:
        print(4)