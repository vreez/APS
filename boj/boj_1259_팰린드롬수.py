import sys; sys.stdin = open("1259.txt", "r")

while True:
    arr = list(input())
    if len(arr) == 1 and arr[0] == '0':
        break
    else:
        N = len(arr)
        flag = True
        for i in range(N//2):
            if arr[i] == arr[N-1-i]:
                continue
            else:
                flag = False
                break
        if flag:
            print("yes")
        else:
            print("no")