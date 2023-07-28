import sys; sys.stdin = open("9782.txt", "r")

cnt = 0
while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    new = arr[1:]
    cnt += 1
    if len(arr) == 1 and arr[0] == 0:
        break
    else:
        if n % 2 == 0:
            answer = (new[n//2-1] + new[n//2]) / 2
        else:
            answer = new[(n+1)//2-1]

        print("Case {}: {:.1f}".format(cnt, answer))