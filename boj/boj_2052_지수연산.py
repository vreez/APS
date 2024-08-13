import sys; sys.stdin = open("2052.txt", "r")

n = int(input())
ans = "%.300f" % 2 ** -n
for i in range(len(ans)-1, 1, -1):
    if ans[i] != "0":
        check = i
        break
print(ans[:check+1])