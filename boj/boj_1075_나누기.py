import sys; sys.stdin = open("1075.txt", "r")

N = int(input())
F = int(input())

N = (N // 100) * 100
for i in range(0, 100):
    if (N + i) % F == 0:
        answer = (N + i) % 100
        if answer > 9:
            print(answer)
        else:
            print("0"+str(answer))
        break