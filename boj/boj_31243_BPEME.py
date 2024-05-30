import sys; sys.stdin = open("31243.txt", "r")

time = 0
arr = []
for i in range(3):
    a, b, c, d = map(int, input().split())
    if a > c:
        c += 24
    if b > d:
        c -= 1
        d += 60
    time = (c - a)*60 + (d-b)
    arr.append(time)

mi_h = min(arr) // 60
mi_m = str(min(arr) % 60)
mi_m = mi_m.zfill(2)

mx_h = max(arr) // 60
mx_m = str(max(arr) % 60)
mx_m = mx_m.zfill(2)

print("{}:{}".format(mi_h, mi_m))
print("{}:{}".format(mx_h, mx_m))