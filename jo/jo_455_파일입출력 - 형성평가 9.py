arr = input()
li = list(arr.split())
long = []
le = 0
for i in range(len(li)):
    if len(li[i]) > le:
        le = len(li[i])
        long = []
        long.append(li[i])
    elif len(li[i]) == le:
        long.append(li[i])
print(len(arr))
print(*long)
