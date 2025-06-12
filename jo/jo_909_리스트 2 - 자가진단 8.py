arr = []
for i in range(5):
    arr.append(input())

new = sorted(arr, reverse=True)
for i in range(5):
    print(new[i])