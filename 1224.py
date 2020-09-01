import sys
sys.stdin = open("1224.txt")

for tc in range(1, 11):
    int(input())
    str_list = input()
    # print(str_list)
    stack = []
    my_list = []
    for i in range(len(str_list)):
        if str_list[i] == '+':
            if len(stack) == 0 or stack[-1] == '(':
                stack.append(str_list[i])
            elif stack[-1] == '*':
                my_list.append(stack[-1])
                stack.pop()
                stack.append(str_list[i])
            elif stack[-1] == '+':
                my_list.append(stack[-1])
                stack.pop()
                stack.append(str_list[i])
        elif str_list[i] == '*':
            if stack[-1] == '*':
                my_list.append(stack[-1])
                stack.pop()
                stack.append(str_list[i])
            else:
                stack.append(str_list[i])
        elif str_list[i] == '(':
            stack.append(str_list[i])
        elif str_list[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                while stack[-1] != '(':
                    my_list.append(stack[-1])
                    stack.pop()
                stack.pop()
        else:
            my_list.append(str_list[i])
    if len(stack) > 0:
        if stack[-1] != '(':
            my_list.append(stack[-1])
            stack.pop()
        else:
            stack.pop()

    stack2 = []
    for j in range(len(my_list)):
        if my_list[j] != '*' and my_list[j] != '+':
            stack2.append(int(my_list[j]))
        elif my_list[j] == '*':
            stack2.append(stack2.pop() * stack2.pop())
        elif my_list[j] == '+':
            stack2.append(stack2.pop() + stack2.pop())

    print("#{} {}".format(tc, stack2[0]))




