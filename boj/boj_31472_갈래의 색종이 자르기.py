import sys; sys.stdin = open("31472.txt", "r")

W = int(input())
ans = (W * 2)**(0.5)
print(int(ans * 4))


