import sys; sys.stdin = open("9063.txt", "r")

N = int(input())
arr_a = []
arr_b = []
for i in range(N):
    a, b = map(int, input().split())
    if a not in arr_a:
        arr_a.append(a)
    if b not in arr_b:
        arr_b.append(b)
print((max(arr_a)-min(arr_a)) * (max(arr_b)-min(arr_b)))
