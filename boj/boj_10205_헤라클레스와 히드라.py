import sys; sys.stdin = open("10205.txt", "r")

data = int(input())

for i in range(data):
    N = int(input())
    arr = list(input())
    for j in range(len(arr)):
        if N == 0:
            break
        else:
            if arr[j] == "c":
                N += 1
            else:
                N -= 1

    print("Data Set {}:".format(i+1))
    print(N)
    print()

