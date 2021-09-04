import sys; sys.stdin = open("11719.txt", "r")

while True:
    try:
        arr = input()
        print(arr)
    except EOFError:
        break