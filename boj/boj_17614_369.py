import sys; sys.stdin = open("17614.txt", "r")

N = int(input())

ans = 0
for i in range(1, N+1):
    ans += str(i).count('3')
    ans += str(i).count('6')
    ans += str(i).count('9')
print(ans)
