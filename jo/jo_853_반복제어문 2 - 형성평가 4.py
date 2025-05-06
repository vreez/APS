arr = list(map(int, input().split()))
avg = round(sum(arr) / len(arr), 2)
print(format(avg, ".2f"))
