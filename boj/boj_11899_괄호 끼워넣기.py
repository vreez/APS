import sys; sys.stdin = open("11899.txt", "r")

arr = list(input())
stack = []
for i in range(len(arr)):
    if arr[i] == ')':
        if len(stack) > 0 and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(arr[i])
    else:
        stack.append(arr[i])
print(len(stack))



