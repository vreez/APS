import sys; sys.stdin = open("2108.txt", "r")
from collections import Counter

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
total = sum(arr)
arr = sorted(arr)
# 산술평균
print(round(total / N))
# 중앙값
print(arr[N//2])
# 최빈값
count = Counter(arr)
often = count.most_common()
print(often)
if len(often) > 1:
    if often[0][1] == often[1][1]:
        print(often[1][0])
    else:
        print(often[0][0])
else:
    print(often[0][0])
# 범위
print(max(arr) - min(arr))