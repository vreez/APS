import sys; sys.stdin = open("5613.txt", "r")

n = 0
temp = []
while True:
    i = input()
    if i == "=":
        break
    if n % 2 == 0:
        i = int(i)
        temp.append(i)
    else:
        temp.append(i)
    n += 1

total = temp[0]
for i in range(1, len(temp)-1):
    if i % 2 != 0:
        if temp[i] == "+":
            total += temp[i+1]
        elif temp[i] == "-":
            total -= temp[i+1]
        elif temp[i] == "/":
            total //= temp[i+1]
        else:
            total *= temp[i+1]

print(total)


