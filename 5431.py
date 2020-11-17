import sys; sys.stdin = open("5431.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    people = [i for i in range(1, N+1)]
    result = []
    for j in range(N):
        if people[j] not in arr:
            result.append(people[j])

    print("#{}".format(tc), end=" ")

    for k in range(len(result)):
        print(result[k], end=" ")
    print()
