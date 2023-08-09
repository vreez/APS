import sys; sys.stdin = open("2587.txt", "r")

total = 0
arr = []

for i in range(5):
    num = int(input())
    total += num
    arr.append(num)

arr = sorted(arr)

print(total//5)
print(arr[2])