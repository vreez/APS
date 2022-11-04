import sys; sys.stdin = open("9610.txt", "r")

N = int(input())
q1, q2, q3, q4, axis = 0, 0, 0, 0, 0
for i in range(N):
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        axis += 1
    elif a > 0 and b > 0:
        q1 += 1
    elif a < 0 and b > 0:
        q2 += 1
    elif a < 0 and b < 0:
        q3 += 1
    else:
        q4 += 1

print("Q1: {}".format(q1))
print("Q2: {}".format(q2))
print("Q3: {}".format(q3))
print("Q4: {}".format(q4))
print("AXIS: {}".format(axis))
