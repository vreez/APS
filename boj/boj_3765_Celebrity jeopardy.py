import sys; sys.stdin = open("3765.txt", "r")

while True:
    try:
        arr = input()
        print(arr)
    except EOFError:
        break