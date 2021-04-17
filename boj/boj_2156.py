import sys; sys.stdin = open("2156.txt", "r")

N = int(input())
arr = list(int(input()) for _ in range(N))
# 포도주 양 맨 앞 0번째 인덱스에 0더하기
arr.insert(0, 0)
# 0번째의 최대값은 0이므로 result에 0더하기
result = [0]
# i가 1일 경우
result.append(arr[1])
# i 가 1보다 클 경우,
if N > 1:
    result.append(arr[1] + arr[2])
for i in range(3, N+1):
    # i 시점에서 최대값이 나올 수 있는 경우는 i-1을 선택했을 경우, i-1을 선택하지 않고, i-2를 선택했을 경우,
    # i-1, i-2를 둘 다 선택한 경우 총 3가지이다. 이 중 가장 큰 값을 골라 선택하면 된다.
    result.append(max(result[i-1], result[i-2] + arr[i], result[i-3] + arr[i-1] + arr[i]))

print(result[N])