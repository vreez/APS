# T = [123, 100]
T = list(map(int, input().split()))

count = 0
if T[1] != T[0]:
    for i in range(1, T[0] - T[1] + 2):
        T[1] += 1
        count += 1
print(count)


