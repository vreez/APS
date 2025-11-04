arr = list(map(int, input().split()))
new = []
for i in range(len(arr)):
    if arr[i] % 5 == 0:
        new.append(arr[i])

print("Multiples of 5 : {}".format(len(new)))
print("sum : {}".format(sum(new)))
avg = sum(new)/len(new)
print("avg : {}".format(round(avg, 1)))