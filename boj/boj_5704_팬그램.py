import sys; sys.stdin = open("5704.txt", "r")

while True:
    arr = list(input())
    alpha = "abcdefghijklmnopqrstuvwxyz"
    check = list(alpha)
    if len(arr) == 1 and arr[0] == "*":
        break
    else:
        for i in range(len(check)):
            if check[i] in arr:
                check[i] = 0
    new = set(check)
    if len(new) == 1:
        print("Y")
    else:
        print("N")
