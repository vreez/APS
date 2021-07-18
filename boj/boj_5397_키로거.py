import sys; sys.stdin = open("input/5397.txt", "r")

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    password = list(sys.stdin.readline().rstrip())
    left = []
    right = []

    for num in password:
        if num == '<':
            if len(left) > 0:
                right.append(left.pop())
        elif num == '>':
            if len(right) > 0:
                left.append(right.pop())
        elif num == '-':
            if len(left) > 0:
                left.pop()
        else:
            left.append(num)
    right.reverse()
    result = left + right

    print(''.join(result))
