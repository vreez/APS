import sys; sys.stdin = open("18414.txt", "r")

X, L, R = map(int, input().split())

num = 0
diff = 100001

for i in range(L, R+1):
    if abs(i - X) < diff:
        num = i
        diff = abs(i - X)

print(num)