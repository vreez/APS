import sys; sys.stdin = open("16561.txt", "r")

n = int(input())//3
ans = ((n-1)*(n-2))//2
print(ans)