import sys; sys.stdin = open("9526.txt", "r")

words = input().split()
for i in range(2):
    print("{}의 키는 {}cm이며, 몸무게는 {:.6f}kg입니다.".format(words[0], int(words[1]), float(words[2])))