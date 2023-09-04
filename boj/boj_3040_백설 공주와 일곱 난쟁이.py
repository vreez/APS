import sys; sys.stdin = open("3040.txt", "r")

num = []
for i in range(9):
    d = int(input())
    num.append(d)
total = sum(num)
check = total - 100
new = sorted(num)

i, j = 0, 8
while i < j:
    s = new[i] + new[j]
    if s == check:
        num.remove(new[i])
        num.remove(new[j])
        break
    elif s > check:
        j -= 1
    else:
        i += 1

for k in range(len(num)):
    print(num[k])
