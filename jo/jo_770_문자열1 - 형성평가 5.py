import sys; sys.stdin = open("770.txt", "r")

name, height, weight = input().split()
new = round(float(weight), 1)
print("{}의 키는 {}cm이며, 몸무게는 {}kg입니다.".format(name, height, new))