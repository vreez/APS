N = int(input())

# 삼각형의 높이 N이 주어진 범위를 벗어날 경우, INPUT ERROR를 출력하고, 다시 입력을 받는다.
# N은 1이상 100이하의 홀수여야 한다.
while N < 1 or N > 100 or N % 2 == 0:
    print("INPUT ERROR")
    N = int(input())

# N의 범위를 만족할 경우
if 1 <= N <= 100 and N % 2 == 1:
    # 출력할 알파벳을 순서대로 저장해둔다.
    words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z']

    # 삼각형을 저장할 이차 배열을 생성한다.
    arr = [[0] * N for _ in range(N)]
    # A부터 Z까지 알파벳을 순차적으로 반복해야 하므로, count를 활용한다.
    count = 0
    # 행의 크기가 유동적이므로 a라는 변수를 활용한다.
    a = 0
    # 가장 중심이 되는 첫 열부터 하나씩 값을 줄여가며 출력한다.
    for j in range(N // 2, -1, -1):
        # 매 열마다 행 값의 범위가 변동되므로 a를 활용한다.(시작값은 1씩 감소, 종료값은 1 증가)
        for i in range(N // 2 - a, N // 2 + 1 + a):
            if 0 <= i < N and 0 <= j < N:
                arr[i][j] = words[count % 26]
                count += 1
        # 행의 값을 변화시켜줄 a는 한 열의 입력이 모두 끝난 후에 1번씩만 증가시킨다.
        a += 1

    # 이중 for문을 활용해, arr[i][j]값이 0일 경우에는 공백을 출력한다.
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                print(" ", end=" ")
            else:
                print(arr[i][j], end=" ")
        print()




