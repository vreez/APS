import sys; sys.stdin = open("2751.txt", "r")

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)

new_arr = sorted(arr)

for i in range(N):
    print(new_arr[i])
