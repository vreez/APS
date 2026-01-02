N = int(input())

for i in range(N):
    name, num = input().split()
    if num == "2026":
        print(name)
        break
