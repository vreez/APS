arr = list(map(int, input().split()))
total = sum(arr)
avg = round(total / len(arr), 1)
print("총점 : {}".format(total))
print("평균 : {}".format(avg))