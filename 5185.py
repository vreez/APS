import sys; sys.stdin = open("5185.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, arr = input().split()

    my_arr = []

    for i in range(int(N)):
        n = int(arr[i], 16)

        my_arr.append(1 if n & 8 else 0)
        my_arr.append(1 if n & 4 else 0)
        my_arr.append(1 if n & 2 else 0)
        my_arr.append(1 if n & 1 else 0)

    print("#{}".format(tc), end=" ")
    for i in range(len(my_arr)):
        print(my_arr[i], end="")
    print()
