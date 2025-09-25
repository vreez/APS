arr = list(map(int, input().split()))
new = []
for i in range(len(arr)):
    new.append(arr[i]//10)

for i in range(100, -10, -10):
    if new.count(i//10):
        print("{} : {} person".format(i, new.count(i//10)))