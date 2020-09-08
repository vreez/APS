# 완전검색(조건에 해당하는 경우를 찾아라)
# 부분 집합과 관련이 있다. (전체 점원 : 전체집합)
# 가지치기 생각해보기
# 최적해 구하기

import sys; sys.stdin = open('1486.txt', 'r')

# 모든 부분집합 구하기
def powerset(n, k, cursum):
    if cursum >= B:
        my_cursum.append(cursum)
        return
    if n == k:
        pass
    else:
        # k번째 선택
        result[k] = 1
        powerset(n, k + 1, cursum + clerk[k])
        # k번째 비선택
        result[k] = 0
        powerset(n, k + 1, cursum)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    clerk = list(map(int, input().split()))
    result = [0] * N
    my_cursum = []
    powerset(N, 0, 0)  # 깊이, 시작값, 값 더하기

    print('#{} {}'.format(tc, (min(my_cursum)-B)))


