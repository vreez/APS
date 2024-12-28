import sys; sys.stdin = open("9528.txt", "r")

words = input().split()
print("{}의 키는 {}cm이며, 몸무게는 {}kg입니다.".format(words[0], int(words[1]), round(float(words[2]), 1)))