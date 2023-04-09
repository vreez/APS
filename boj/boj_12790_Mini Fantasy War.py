import sys; sys.stdin = open("12790.txt", "r")

T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    hp = arr[0] + arr[4]
    mp = arr[1] + arr[5]
    sp = arr[2] + arr[6]
    dp = arr[3] + arr[7]
    if hp < 1:
        hp = 1
    if mp < 1:
        mp = 1
    if sp < 0:
        sp = 0
    print(1*hp + 5*mp + 2*sp + 2*dp)