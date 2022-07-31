import sys; sys.stdin = open("3512.txt", "r")

n, c = map(int, input().split())

total = 0
bedroom = 0
balcony = 0
cost = 0
for i in range(n):
    a, t = input().split()
    total += int(a)
    if t == "bedroom":
        bedroom += int(a)
    if t == "balcony":
        balcony += int(a)

cost = (total - (balcony / 2)) * c

print(total)
print(bedroom)
print(cost)