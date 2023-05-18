import sys; sys.stdin = open("25814.txt", "r")

first, second = input().split()
fw = len(first)
sw = len(second)
first = list(first)
second = list(second)

sf = 0
ss = 0
for i in range(fw):
    sf += int(first[i])

for j in range(sw):
    ss += int(second[j])

if fw*sf > sw*ss:
    print(1)
elif sw*ss > fw*sf:
    print(2)
else:
    print(0)
