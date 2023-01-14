import sys; sys.stdin = open("26350.txt", "r")

N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    flag = True
    for j in range(1, arr[0]):
        if arr[j] * 2 > arr[j+1]:
            flag = False
    answer = ' '.join(map(str, arr[1:]))
    if flag == True:
        print("Denominations: {}".format(answer))
        print("Good coin denominations!")
        print()
    else:
        print("Denominations: {}".format(answer))
        print("Bad coin denominations!")
        print()