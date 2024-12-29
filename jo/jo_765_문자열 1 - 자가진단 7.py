import sys; sys.stdin = open("765.txt", "r")

name = input()
num = int(input())
avg = float(input())

print("I am {}(IDNo. {}). I got {:.2f} in my midterm exam.".format(name, num, round(avg, 2)))