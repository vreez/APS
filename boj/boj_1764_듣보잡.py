import sys; sys.stdin = open("input/1764.txt", "r")

N, M = map(int, input().split())
hear = sorted(list(input() for _ in range(N)))
watch = sorted(list(input() for _ in range(M)))

result = {}
for i in range(N):
    if hear[i] not in result:
        result[hear[i]] = 1

for j in range(M):
    if watch[j] in result:
        result[watch[j]] += 1

count = 0
for number in result.values():
    if number == 2:
        count += 1
print(count)

for people, number in sorted(result.items()):
    if number == 2:
        print(people)



