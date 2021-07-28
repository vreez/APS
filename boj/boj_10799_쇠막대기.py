import sys; sys.stdin = open("input/10799.txt" ,"r")

bracket = list(input())

stack = []
lazer = []
iron = []

for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append([bracket[i], i])
    else:
        index = stack.pop()[1]
        if i - index == 1:
            lazer.append(index)
        else:
            iron.append([index, i])

count = 0
for i in range(len(iron)):
    piece = 1
    for j in range(len(lazer)):
        if iron[i][0] < lazer[j] and  iron[i][1] > lazer[j]:
            piece += 1
    count += piece

print(count)

