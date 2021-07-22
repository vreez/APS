import sys; sys.stdin = open("input/10828.txt", "r")

N = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().rstrip().split(' ') for _ in range(N))
stack = []

for i in range(N):
    if arr[i][0] == 'push':
        stack.append(arr[i][1])
    elif arr[i][0] == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif arr[i][0] == 'size':
        print(len(stack))
    elif arr[i][0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    else:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
