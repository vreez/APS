import sys; sys.stdin = open("25801.txt", "r")
alpha = {
    'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0,
    'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0,
    'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0,
    'y':0, 'z':0
}

N = list(input())
for i in range(len(N)):
    alpha[N[i]] += 1

result = []
for key, value in alpha.items():
    if value != 0:
        if value % 2:
            result.append(1)
        else:
            result.append(0)

answer = list(set(result))
if len(answer) == 1:
    print(answer[0])
else:
    print("0/1")
