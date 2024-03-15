import sys; sys.stdin = open("9299.txt", "r")
N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    print("Case {}: {}".format(i+1, arr[0]-1), end=" ")
    new = arr[1:]
    for j in range(arr[0]):
        print(new[j]*(arr[0]-j), end=" ")
    print()
