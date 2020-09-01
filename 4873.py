import sys
sys.stdin = open("4873.txt")

def Forth(arr):
    stack = []

    for i in range(len(arr)):
        if arr[0] == '+' or arr[0] == '-' or arr[0] == '*' or arr[0] == '/' or arr[0] == '.':
            return 'error'
        elif i == len(arr)-1:
            if len(stack) > 1:
                return 'error'
        elif i == len(arr) - 2 and (arr[i] != '+' and arr[i] != '-' and arr[i] != '*' and arr[i] != '/'):
            return 'error'
        elif 0 < i < len(arr)-1 and len(stack) == 1 and (arr[i+1] == '.' or arr[i] == '+' or arr[i] == '-' or arr[i] == '*' or arr[i] == '/'):
            return 'error'
        elif 0 < i < len(arr)-1 and len(stack) > 1 and (arr[i+1] == '.' and arr[i] != '+' and arr[i] != '-' and arr[i] != '*' and arr[i] != '/'):
            return 'error'
        if arr[i] == '+':
            stack.append(stack.pop(-2) + stack.pop(-1))
        elif arr[i] == '-':
            stack.append(stack.pop(-2) - stack.pop(-1))
        elif arr[i] == '*':
            stack.append(stack.pop(-2) * stack.pop(-1))
        elif arr[i] == '/':
            stack.append(stack.pop(-2) // stack.pop(-1))
        elif arr[i] == '.':
            return stack[0]
        elif arr[i] == '.':
            if len(stack) > 1:
                return 'error'
        else:
            stack.append(int(arr[i]))

T = int(input())
for tc in range(1, T+1):
    my_list = list(map(str, input().split()))

    print("#{} {}".format(tc, Forth(my_list)))