import sys; sys.stdin = open("18429.txt", "r")
import itertools

N, K = map(int, input().split())
arr = list(map(int, input().split()))
# 운동 키트의 중량 증가량을 가지고 만들 수 있는 모든 경우를 구해 list에 저장한다.
exercise = list(itertools.permutations(arr, N))
count = 0
for i in range(len(exercise)):
    check = 0
    weight = 500
    for j in range(N):
        if weight - K + exercise[i][j] < 500:
            break
        else:
            check += 1
            weight = weight - K + exercise[i][j]
    if check == N:
        count += 1
print(count)



