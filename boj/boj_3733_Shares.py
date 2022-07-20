import sys; sys.stdin = open("3733.txt", "r")

while True:
    try:
        N, S = map(int, input().split())
        answer = S // (N + 1)
        print(answer)
    except EOFError:
        break