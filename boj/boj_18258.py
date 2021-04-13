import sys;
from collections import deque
N = int(sys.stdin.readline())
arr = list(sys.stdin.readline().split() for _ in range(N))
queue = deque()
for i in range(N):
    if arr[i][0] == 'push':
        # arr[i] = arr[i].replace('push ', '')
        queue.append(arr[i][1])
    elif arr[i][0] == 'front' and len(queue) > 0:
        print(int(queue[0]))
    elif arr[i][0] == 'front' and len(queue) == 0:
        print(-1)
    elif arr[i][0] == 'back' and len(queue) > 0:
        print(queue[-1])
    elif arr[i][0] == 'back' and len(queue) == 0:
        print(-1)
    elif arr[i][0] == 'pop' and len(queue) > 0:
        print(str(queue.popleft()))
    elif arr[i][0] == 'pop' and len(queue) == 0:
        print(-1)
    elif arr[i][0] == 'size':
        print(len(queue))
    elif arr[i][0] == 'empty' and len(queue) > 0:
        print(0)
    elif arr[i][0] == 'empty' and len(queue) == 0:
        print(1)