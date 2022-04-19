import sys; sys.stdin = open("1102.txt", "r")

N = int(input())
stack = []
for i in range(N):
    M = input().split()
    if M[0] == 'i':
        stack.append(M[1])
    elif M[0] == 'c':
        print(len(stack))
    elif M[0] == 'o':
        if len(stack) == 0:
            print('empty')
        else:
            print(stack[-1])
            stack.pop()




