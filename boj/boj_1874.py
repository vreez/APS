import sys; sys.stdin = open("1874.txt", "r")

N = int(input())
arr = list(int(input()) for _ in range(N))

stack = []
result = []
num = 1
check = True
for i in range(N):
    while num <= arr[i]:
        stack.append(num)
        result.append('+')
        num += 1
    if stack[-1] == arr[i]:
        stack.pop()
        result.append('-')
    else:
        check = False
        break

if check == False:
    print('NO')
else:
    for i in range(len(result)):
        print(result[i])
