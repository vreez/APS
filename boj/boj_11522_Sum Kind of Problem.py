import sys; sys.stdin = open("11522.txt", "r")

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    s1 = b*(b+1)//2
    s2 = b*b
    s3 = s2+b
    print(a, s1, s2, s3)