import sys; sys.stdin = open("9076.txt", "r")

N = int(input())
for _ in range(N):
    arr = sorted(list(map(int, input().split())))
    new = arr[1:len(arr)-1]

    if new[-1] - new[0] >= 4:
        print("KIN")
    else:
        print(sum(new))
