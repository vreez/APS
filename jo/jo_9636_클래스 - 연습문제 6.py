arr = []
for i in range(5):
    name, height, weight = input().split()
    arr.append([name, height, weight])

arr.sort(key=lambda x:x[1])
for i in range(5):
    print("{} {} {}".format(arr[i][0], arr[i][1], arr[i][2]))
print()
arr.sort(key=lambda x:x[2], reverse=True)
for i in range(5):
    print("{} {} {}".format(arr[i][0], arr[i][1], arr[i][2]))
print()
arr.sort(key=lambda x:x[0])
for i in range(5):
    print("{} {} {}".format(arr[i][0], arr[i][1], arr[i][2]))