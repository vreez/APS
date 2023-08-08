import sys; sys.stdin = open("2592.txt", "r")

total = 0
dict = {}
for i in range(10):
    num = int(input())
    total += num
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
max_key = max(dict, key=dict.get)

print(total // 10)
print(max_key)
