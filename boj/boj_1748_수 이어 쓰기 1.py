import sys; sys.stdin = open("input/1748.txt", "r")

N = input()

count = 0
if len(N) < 2:
    count = int(N)
else:
    for i in range(len(N)-1):
        count += (i + 1) * 9 * (10 ** i)
    count += len(N) * (int(N) - 10 ** (len(N) - 1) + 1)
print(count)
