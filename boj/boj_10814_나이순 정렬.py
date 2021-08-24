import sys; sys.stdin = open("10814.txt", "r")

N = int(input())
people = [list(input().split()) for _ in range(N)]
for i in range(len(people)):
    people[i][0] = int(people[i][0])
    people[i].append(i)

answer = sorted(people, key = lambda x : (x[0], x[2]))

for i in range(len(answer)):
    print(answer[i][0], answer[i][1])