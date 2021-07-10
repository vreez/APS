import sys; sys.stdin = open("input/9375.txt")

testCase = int(input())
for _ in range(testCase):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    clothes = {}
    # for문을 사용해서 종류별 의복의 개수를 dictionary 형태로 저장한다.
    for i in range(N):
        if arr[i][1] not in clothes:
            clothes[arr[i][1]] = 1
        else:
            clothes[arr[i][1]] += 1
    # 옷을 단 하나라도 입어야 하기 때문에
    # 모든 경우(옷을 입거나 입지 않거나)에서 옷을 아무것도 입지 않은 상태 1가지를 빼준다.
    total = 1
    for count in clothes.values():
        total *= (count + 1)
    total = total - 1

    print(total)
