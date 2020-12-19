n, m = map(int, input().split())

# n의 크기가 100이하의 홀수가 아니고 m이 1과 4사이의 정수가 아니면
# INPUT ERROR를 출력하고, n과 m을 새롭게 입력받는다.
while n > 100 or n % 2 == 0 or m < 1 or m > 4:
    print('INPUT ERROR!')
    n, m = map(int, input().split())

# m이 1일 때
if m == 1:
    a = 1
    for i in range(n):
        for j in range(a):
            print('*', end='')
        print()
        # 행이 n // 2가 되기 전까지 열 값을 하나씩 증가시킨다.
        if i < n // 2:
            a += 1
        # n // 2가 되면 열의 범위에 해당하는 a 값을 하나씩 감소시킨다.
        else:
            a -= 1
# m이 2일 때
elif m == 2:
    # 처음부터 값을 채우는 것이 아니므로 배열을 만들어 저장한 후, '*'에 해당하는 값만 출력한다.
    arr = [[0] * (n // 2 + 1) for _ in range(n)]
    b = n // 2 + 1
    a = n // 2
    for i in range(n):
        for j in range(a, b):
            arr[i][j] = '*'
        # 행이 n // 2 보다 작을 때까지 열의 시작값을 하나씩 감소시킨다.
        if i < n // 2:
            a -= 1
        # n // 2행부터 열의 시작값인 a값을 다시 하나씩 증가시킨다.
        else:
            a += 1
    # arr에서 '*'에 해당하는 값만 출력한다.
    for i in range(n):
        for j in range(n // 2 + 1):
            if arr[i][j] == 0:
                print(' ', end='')
            else:
                print(arr[i][j], end='')
        print()
# m이 3일 때
elif m == 3:
    # 배열 arr를 생성한다.
    arr = [[0] * n for _ in range(n)]
    a = 0
    b = n
    for i in range(n):
        # a를 각 행의 시작값으로 b를 끝값으로 지정하며 n // 2지점에 이르기 전까지
        # 시작값 a를 하나씩 증가시키고, b값을 하나씩 감소시킨다.
        for j in range(a, b):
            arr[i][j] = '*'
        if i < n // 2:
            a += 1
            b -= 1
        # 행의 값이 n // 2보다 같거나 커지면 시작값 a를 감소시키고, 끝값 b를 하나씩 증가시킨다.
        else:
            a -= 1
            b += 1
    # arr에서 '*'에 해당하는 부분만 출력하고 0에 해당하는 값은 공백으로 출력한다.
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                print(' ', end='')
            else:
                print(arr[i][j], end='')
        print()
# m이 4일 때
else:
    # 배열 arr를 생성한다.
    arr = [[0] * n for _ in range(n)]
    # a는 각행의 시작값
    # b는 끝값을 의미한다.
    a = 0
    b = n // 2 + 1
    for i in range(n):
        for j in range(a, b):
            arr[i][j] = '*'
        # 행의 값이 n // 2보다 작으면 시작값을 하나씩 증가시키고 끝값은 유지한다.
        if i < n // 2:
            a += 1
        # 행의 값이 n // 2와 같아지거나 그 이상이면 시작값을 유지하고 끝값을 하나씩 증가시킨다.
        else:
            b += 1
    # 배열 arr를 하나씩 돌며 값이 '*'인 경우에만 출력한다.
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                print(' ', end='')
            else:
                print(arr[i][j], end='')
        print()



