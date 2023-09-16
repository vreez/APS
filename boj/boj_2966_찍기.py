import sys; sys.stdin = open("2966.txt", "r")

N = int(input())
arr = list(input())

A = ["A", "B", "C"]
B = ["B", "A", "B", "C"]
G = ["C", "C", "A", "A", "B", "B"]
newA = A*N
newB = B*N
newG = G*N
count = [0, 0, 0]
for i in range(N):
    if arr[i] == newA[i]:
        count[0] += 1
    if arr[i] == newB[i]:
        count[1] += 1
    if arr[i] == newG[i]:
        count[2] += 1
print(max(count))
if max(count) == count[0]:
    print("Adrian")
if max(count) == count[1]:
    print("Bruno")
if max(count) == count[2]:
    print("Goran")
