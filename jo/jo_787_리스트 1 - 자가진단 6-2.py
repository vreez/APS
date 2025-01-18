arr1 = []
arr2 = []
for i in range(6):
    if i % 2 == 0:
        arr1.append(input())
    else:
        arr2.append(input())
new = arr1+arr2
print("Element? Element? Element? Element? Element? Element?", end=" ")
print(new)