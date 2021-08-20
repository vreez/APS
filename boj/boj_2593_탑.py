import sys; sys.stdin = open("2593.txt", "r")

N = int(input())
tops = list(map(int, input().split()))
result = [0] * N
stack = [[tops[-1], N-1]]
for i in range(N-2, -1, -1):
    while len(stack) > 0:
        if tops[i] >= stack[-1][0]:
            result[stack[-1][1]] = i + 1
            stack.pop()
        else:
            break
    stack.append([tops[i], i])
for num in result:
    print(num, end=' ')