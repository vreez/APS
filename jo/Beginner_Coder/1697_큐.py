import sys; sys.stdin = open("1697.txt", "r")

N = int(input())
queue = []
for i in range(N):
    M = input().split()
    if M[0] == 'i':
        queue.append(M[1])
    elif M[0] == 'c':
        print(len(queue))
    elif M[0] == 'o':
        if len(queue) == 0:
            print('empty')
        else:
            print(queue[0])
            queue.pop(0)




