N, M = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
max = 0

# N개의 카드 가운데 3장을 뽑아 만든 수 가운데 M을 넘지 않는 가장 큰 수를 출력해야 하므로
# 모든 경우의 수를 구한 뒤에, 조건에 맞는 수를 출력하는 방식으로 문제를 해결한다.

# 모든 경우의 수를 다 구하기 위하여, 첫번째 숫자의 범위는 인덱스 0부터 N-3까지
for i in range(N-2):
    total += arr[i]
    # 두번째 숫자의 범위는 첫번째 숫자로 뽑인 카드의 다음 인덱스부터 N-2까지
    for j in range(i+1, N-1):
        total += arr[j]
        # 마지막 숫자의 범위는 두번째 카드 다음 인덱스부터 마지막까지로 정의한다.
        for k in range(j+1, N):
            total += arr[k]
            # M을 넘지 않는 수 가운데 가장 큰 수를 출력해야 하므로, max를 설정하고
            # 뽑힌 숫자의 합을 의미하는 total과 max를 비교하여 total값이 M보다 크지 않고, max보다 크면
            # 해당 total값을 새로운 max값으로 지정한다.
            if total > max and total <= M:
                max = total
            # for문은 정해진 범위를 모두 반복하므로, 하나의 total이 완성(숫자 3개를 모두 선택)되면
            # 다음 숫자로 넘어가기 전 새롭게 더해진 숫자 값을 total에서 빼준다.
            total -= arr[k]
        total -= arr[j]
    total -= arr[i]

print(max)
