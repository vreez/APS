import sys; sys.stdin = open("15784.txt", "r")

N, a, b = map(int, input().split())
list1 = []
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    list1.append(arr[i][b-1])
list2 = arr[a-1]

if max(list1) > arr[a-1][b-1] or max(list2) > arr[a-1][b-1]:
    print("ANGRY")
else:
    print("HAPPY")