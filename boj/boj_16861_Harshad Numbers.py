import sys; sys.stdin = open("16861.txt", "r")

N = input()
while True:
    checkList = list(map(int, N))
    if int(N) % sum(checkList):
        N = str(int(N) + 1)
    else:
        print(N)
        break