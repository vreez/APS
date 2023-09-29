import sys; sys.stdin = open("29163.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
odd = 0
even = 0
for i in range(N):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1
if even > odd:
    print("Happy")
else:
    print("Sad")
