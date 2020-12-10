N = int(input())

# 출력할 알파벳을 순서대로 저장해둔다.
words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z']

# 알파벳을 담을 이차 배열을 만든다.
arr = [[0] * N for _ in range(N)]

# count를 사용하여 순서에 맞는 알파벳을 담는다.
count = 0
# i는 열, j는 행을 의미한다.
for i in range(N):
    for j in range(N):
        # 열(i)이 홀수일 경우, 가장 아래 행부터 위로 하나씩 알파벳을 채워나가야 하므로,
        # 행(j)은 N에서 1을 뺀 숫자에서 행(j)의 값을 뺀 N - 1 - j가 된다.
        if i % 2 != 0:
            j = N - 1 - j
            # a부터 z까지 모두 사용하였으면, 이어서 다시 a를 출력해야하므로 count를 26으로 나눈
            # 나머지를 활용한다.
            arr[j][i] = words[count % 26]
            # 알파벳의 순서를 하나씩 증가시킨다.
            count += 1
        # 열(i)이 짝수일 경우
        else:
            arr[j][i] = words[count % 26]
            count += 1

for lst in arr:
    print(*lst)