total = 0
for _ in range(4):
    record = int(input())
    total += record

if total + 300 <= 1800:
    print("Yes")
else:
    print("No")