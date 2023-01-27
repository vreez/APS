import sys; sys.stdin = open("5073.txt", "r")

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0 and arr[0] == arr[1] and arr[1] == arr[2]:
        break
    else:
        new = sorted(arr)
        if new[2] >= new[0] + new[1]:
            print("Invalid")
        else:
            check = set(new)
            if len(check) == 1:
                print("Equilateral")
            elif len(check) == 2:
                print("Isosceles")
            else:
                print("Scalene")