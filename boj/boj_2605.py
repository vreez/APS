T = int(input())
students = list(map(int, input().split()))

new = []
for i in range(len(students)):
    if students[i] == 0:
        new += [i + 1]
    else:
        new.insert(-students[i], i+1)
for n in new:
    print(n, end=' ')
