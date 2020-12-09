N = int(input())

# 출력할 알파벳을 순서대로 저장해둔다.
words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z']

# N*N의 크기의 배열을 만든다.
arr = [[0] * N for _ in range(N)]

# count를 세어 인덱스로 활용한다.
count = 0
for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        # 나머지를 활용하여 카운트가 알파벳의 총 숫자인 26개를 넘어가면 다시 A부터 출력하도록 한다.
        arr[j][i] = words[count % 26]
        count += 1

# 하나씩 공백을 두고 출력한다.
for w in arr:
    print(*w)

