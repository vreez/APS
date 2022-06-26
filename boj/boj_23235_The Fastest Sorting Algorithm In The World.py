import sys; sys.stdin = open("23235.txt", "r")

check = 0
cnt = 0
while check == 0:
    arr = list(map(int, input().split()))
    if len(arr) == 1 and arr[0] == 0:
        check = 1
        break
    cnt += 1
    print("Case {}: Sorting... done!".format(cnt))