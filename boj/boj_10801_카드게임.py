import sys; sys.stdin = open("10801.txt", "r")

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

A = 0
B = 0
for i in range(10):
    if arr1[i] > arr2[i]:
        A += 1
    elif arr1[i] < arr2[i]:
        B += 1
    else:
        A += 1
        B += 1

if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("D")