arr = list(map(int, input().split()))
total = sum(arr)
avg = round(sum(arr)/len(arr), 1)

print("avg : {}".format(avg))
if avg >= 80:
    print("pass")
else:
    print("fail")
