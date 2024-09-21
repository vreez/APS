import sys; sys.stdin = open("21567.txt", "r")

A = int(input())
B = int(input())
C = int(input())

res = A * B * C
new = str(res)
ans = [0]*10
for i in new:
    if i == '0':
        ans[0] += 1
    elif i == '1':
        ans[1] += 1
    elif i == '2':
        ans[2] += 1
    elif i == '3':
        ans[3] += 1
    elif i == '4':
        ans[4] += 1
    elif i == '5':
        ans[5] += 1
    elif i == '6':
        ans[6] += 1
    elif i == '7':
        ans[7] += 1
    elif i == '8':
        ans[8] += 1
    else:
        ans[9] += 1
for i in range(10):
    print(ans[i])