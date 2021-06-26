import sys; sys.stdin = open("input/4796.txt", "r")
# 인덱스 설정 위치에 유의하기
index = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    result = (V // P * L) + min((V % P), L)
    print("Case {}: {}".format(index, result))
    index += 1