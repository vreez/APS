import sys; sys.stdin = open("13420.txt", "r")

N = int(input())
for i in range(N):
    arr = list(input().split())
    if arr[1] == "+":
        if int(arr[0]) + int(arr[2]) == int(arr[4]):
            print("correct")
        else:
            print("wrong answer")
    elif arr[1] == "-":
        if int(arr[0]) - int(arr[2]) == int(arr[4]):
            print("correct")
        else:
            print("wrong answer")
    elif arr[1] == "*":
        if int(arr[0]) * int(arr[2]) == int(arr[4]):
            print("correct")
        else:
            print("wrong answer")
    else:
        if int(arr[0]) // int(arr[2]) == int(arr[4]):
            print("correct")
        else:
            print("wrong answer")