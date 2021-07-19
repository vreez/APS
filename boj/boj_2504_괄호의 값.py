import sys; sys.stdin = open("input/2504.txt", "r")

arr = list(input())
stack = []
num = []
answer = True
for i in range(len(arr)):
    if arr[i] == '(' or arr[i] == '[':
        stack.append(arr[i])
    elif arr[i] == ')':
        if len(stack) > 0:
            if stack[-1] != '(':
                num = 0
                while stack and stack[-1] != '(':
                    if stack[-1] == '[':
                        answer = False
                        break
                    else:
                        num += stack[-1]
                        stack.pop()
                # []())와 같은 경우 위의 while문을 통과하면 stack이 0이 되지만
                # )의 짝이 없기 때문에 결과적으로는 잘못된 괄호이므로 False 표시를 해준다.
                if len(stack) == 0:
                    answer = False
                    break
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(num * 2)
            elif stack[-1] == '(':
                stack.pop()
                stack.append(2)
    elif arr[i] == ']':
        if len(stack) > 0:
            if stack[-1] != '[':
                num = 0
                while stack and stack[-1] != '[':
                    if stack[-1] == '(':
                        answer = False
                        break
                    else:
                        num += stack[-1]
                        stack.pop()
                if len(stack) == 0:
                    answer = False
                    break
                if stack[-1] == '[':
                    stack.pop()
                    stack.append(num * 3)
            elif stack[-1] == '[':
                stack.pop()
                stack.append(3)

result = 0
for i in range(len(stack)):
    if stack[i] == '(' or stack[i] == '[':
        answer = False
    else:
        result += stack[i]

if answer == False:
    print(0)
else:
    print(result)


