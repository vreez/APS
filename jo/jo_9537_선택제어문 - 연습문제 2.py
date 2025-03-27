import sys; sys.stdin = open("9537.txt", "r")

a, b = map(int, input().split())
if a >= b:
    small = b
    big = a
else:
    small = a
    big = b
print("입력받은 수 중 큰 수는 {} 이고 작은 수는 {} 입니다.".format(big, small))