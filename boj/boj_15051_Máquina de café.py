import sys; sys.stdin = open("15051.txt", "r")

A = int(input())
B = int(input())
C = int(input())

setting_A = (2*B) + (4*C)
setting_B = (2*A) + (2*C)
setting_C = (4*A) + (2*B)
check = [setting_A, setting_B, setting_C]

print(min(check))