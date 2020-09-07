# 패턴매칭
# 찾아야 하는 문자열의 길이만큼 뺀 것 까지 인덱스로 둔다.(교수님 해설)

# 특수문자가 들어가서 생긴 인코딩 에러
import sys; sys.stdin =open('1213.txt', 'r', encoding='UTF8')

for tc in range(1, 11):
    a = int(input())
    N = input()
    M = input()
    n = len(N)
    m = len(M)

    # 항상 확인해보는 습관 중요!
    # print(N)
    # print(M)
    # print(n)
    # print(m)

    cnt = 0
    for i in range(0, m):
        if M[i:i+n] == N:
            # print(M[i:i+n])
            cnt += 1
    print("#{} {}".format(tc, cnt))
