import sys; sys.stdin = open("input/10866.txt", "r")

N = int(input())
order = list(input().split( ) for _ in range(N))

deque = []
for i in range(N):
    if order[i][0] == 'push_front':
        deque.insert(0, order[i][1])
    elif order[i][0] == 'push_back':
        deque.append(order[i][1])
    elif order[i][0] == 'pop_front':
        if len(deque) > 0:
            print(deque[0])
            deque.pop(0)
        else:
            print(-1)
    elif order[i][0] == 'pop_back':
        if len(deque) > 0:
            print(deque[-1])
            deque.pop()
        else:
            print(-1)
    elif order[i][0] == 'size':
        print(len(deque))
    elif order[i][0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif order[i][0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    else:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])