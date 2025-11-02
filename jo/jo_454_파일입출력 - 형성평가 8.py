n = int(input())
result = []
for i in range(n):
    a, b, c = map(int, input().split())
    avg = round((a+b+c) / 3, 1)
    result.append(avg)

new = sorted(result, reverse=True)
for i in range(n):
    print(new[i])
