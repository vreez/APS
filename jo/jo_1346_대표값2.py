import sys; sys.stdin = open("1346.txt", "r")

arr = []
for _ in range(5):
    num = int(input())
    arr.append(num)

new = sorted(arr)
print(sum(arr)//5)
print(new[2])