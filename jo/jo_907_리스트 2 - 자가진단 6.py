arr = list(map(int, input().split()))
totalA = 0
totalB = 0
for i in range(10):
    if i % 2 == 0:
        totalA += arr[i]
    else:
        totalB += arr[i]

print("sum : {}".format(totalB))
print("avg : {}".format(round(totalA/5, 1)))