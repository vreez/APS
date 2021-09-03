import sys; sys.stdin = open("10845.txt", "r")
from collections import deque

N = int(sys.stdin.readline())
order = []
for i in range(N):
    order.append(sys.stdin.readline().rstrip().split())
queue = deque()
for i in range(N):
    if order[i][0] == 'push':
        queue.append(int(order[i][1]))
    elif order[i][0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif order[i][0] == 'size':
        print(len(queue))
    elif order[i][0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[i][0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order[i][0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])