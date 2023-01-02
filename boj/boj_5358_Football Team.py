import sys; sys.stdin = open("5358.txt", "r")

while True:
    try:
        name = list(input())
        for i in range(len(name)):
            if name[i] == 'e':
                name[i] = 'i'
            elif name[i] == 'i':
                name[i] = 'e'
            elif name[i] == 'E':
                name[i] = 'I'
            elif name[i] == 'I':
                name[i] = 'E'
        print(''.join(name))

    except EOFError:
        break
