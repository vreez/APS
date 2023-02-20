import sys; sys.stdin = open("4806.txt", "r")

cnt = 0
while True:
    try:
        arr = input()
        cnt += 1
    except EOFError:
        break
print(cnt)