import sys; sys.stdin = open("993.txt", "r")

name = input()
num = int(input())
avg = float(input())

print("I am {}(IDNo. {}). I got {:.6f} in my midterm exam.".format(name, num, avg))