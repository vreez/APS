N = int(input())

# 삼각형의 높이 N이 100이하의 양의 홀수가 아닌 경우 INPUT ERROR를 출력하고, 새롭게 N을 입력받는다.
while 0 > N or N > 100 or N % 2 == 0:
    print('INPUT ERROR!')
    N = int(input())

# 높이가 N이고 너비값이 1 + (3 * (N//2))인 arr를 생성한다.
# 행의 최대값인 1 + (3 * (N//2))를 너비값으로 지정한다.
arr = [[0] * (1 + (3 * (N // 2))) for _ in range(N)]

# 각 행의 시작값인 a는 0으로, 범위를 나타내는 값인 b는 1로 시작한다.
a = 0
b = 1

for i in range(N):
    for j in range(a, a + b):
        arr[i][j] = '*'
    # 행의 값이 N // 2 보다 작으면 시작값이 a와 범위인 b를 각각 1과 2만큼 증가시킨다.
    if i < N // 2:
        a += 1
        b += 2
    # 행의 값이 N // 2 보다 같거나 크면 시작값과 범위를 각각 1과 2만큼씩 감소시킨다.
    else:
        a -= 1
        b -= 2

# arr를 하나씩 순환하며 0일 경우는 공백을 *일 경우는 *을 출력한다.
for i in range(N):
    for j in range(1 + (3 * (N//2))):
        if arr[i][j] != '*':
            print(' ', end='')
        else:
            print('*', end='')
    print()
