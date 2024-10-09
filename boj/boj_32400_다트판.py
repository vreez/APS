import sys; sys.stdin = open("32400.txt", "r")

arr = list(map(int, input().split()))
twe = arr.index(20)
a = 0
b = 0
if twe == 0:
    a = (arr[-1] + arr[0] + arr[1]) / 3
elif twe == 19:
    a = (arr[0] + arr[19] + arr[18]) / 3
else:
    a = (arr[twe-1] + arr[twe] + arr[twe+1]) / 3

b = sum(arr) / 20

if a > b:
    print("Alice")
elif b > a:
    print("Bob")
else:
    print("Tie")