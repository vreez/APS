import sys; sys.stdin = open("6825.txt", "r")

weight = float(input())
height = float(input())

BMI = weight / (height * height)

if BMI > 25:
    print("Overweight")
elif BMI >= 18.5 and BMI <= 25:
    print("Normal weight")
else:
    print("Underweight")