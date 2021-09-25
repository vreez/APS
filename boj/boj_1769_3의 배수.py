import sys; sys.stdin = open("1769.txt", "r")

num = list(input())

count = 0
while len(num) > 1:
    total = 0
    count += 1
    for i in range(len(num)):
        total += int(num[i])
    num = list(str(total))

print(count)
if int(num[0]) % 3 == 0:
    print('YES')
else:
    print('NO')

