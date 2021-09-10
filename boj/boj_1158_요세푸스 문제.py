import sys; sys.stdin = open("1158.txt", "r")
from collections import deque

N, K = map(int, input().split())
queue = deque()
for i in range(1, N + 1):
    queue.append(i)

result = []
while len(result) < N:
    queue.rotate(-(K-1))
    result.append(queue.popleft())

print('<', end='')
for i in range(len(result)):
    if i != len(result) - 1:
        print(result[i], end='')
        print(',', end=' ')
    else:
        print(result[i], end='')
print('>')
