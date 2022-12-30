import sys; sys.stdin = open("5357.txt", "r")

N = int(input())
for i in range(N):
    answer = ''
    arr = list(input())
    for j in range(len(arr)):
        if len(answer) == 0:
            answer += arr[j]
        else:
            if answer[-1] != arr[j]:
                answer += arr[j]

    print(answer)