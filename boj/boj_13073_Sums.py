import sys; sys.stdin = open("13073.txt", "r")

N = int(input())
for i in range(N):
    num = int(input())
    s1 = (num*(num+1)) // 2
    s2 = num**2
    s3 = (num**2) + num
    print(s1, s2, s3)