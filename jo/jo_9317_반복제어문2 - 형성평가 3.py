n = int(input())
total = 0
for i in range(1, n+1):
    if i % 5 == 0:
        total += i
        print(i, end=" ")
print()
print(total)