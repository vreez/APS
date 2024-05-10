import sys; sys.stdin = open("4388.txt", "r")

while True:
    a, b = input().split()
    if a == b and a == '0':
        break
    else:
        if len(a) > len(b):
            b = '0'*(len(a)-len(b)) + b
        elif len(b) > len(a):
            a = '0'*(len(b)-len(a)) + a
    carry = 0
    cnt = 0
    for i in range(len(a)-1, -1, -1):
        if int(a[i]) + int(b[i]) + carry >= 10:
            cnt += 1
            carry += 1
        else:
            carry = 0
    print(cnt)

