import sys; sys.stdin = open("input/4949.txt", "r")

while True:
    sentence = list(input())
    if len(sentence) == 1 and sentence[0] == '.':
        break
    stack = []
    answer = 'yes'
    for i in range(len(sentence)):
        if sentence[i] == '(' or sentence[i] == '[':
            stack.append(sentence[i])
        elif sentence[i] == ')':
            if len(stack) == 0:
                answer = 'no'
                break
            elif stack[-1] == '(':
                stack.pop()
            elif stack[-1] == '[':
                answer = 'no'
                break
        elif sentence[i] == ']':
            if len(stack) == 0:
                answer = 'no'
                break
            elif stack[-1] == '[':
                stack.pop()
            elif stack[-1] == '(':
                answer = 'no'
                break
    if len(stack) > 0:
        answer = 'no'

    print(answer)


