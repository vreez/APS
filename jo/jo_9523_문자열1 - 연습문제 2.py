import sys; sys.stdin = open("9523.txt", "r")

a, b, c = input().split()
ans1= a+b+c
ans2 = int(a) + int(b) + int(c)
print("잘못된 결과 : {}".format(ans1))
print("올바른 결과 : {}".format(ans2))