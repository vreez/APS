print("주사위를 던진 결과를 입력하세요.", end=" ")
a, b = map(int, input().split())
if a >= 4 and b >= 4:
    print("이겼습니다.")
elif (a >= 4 and b < 4) or (a < 4 and b >= 4):
    print("비겼습니다.")
else:
    print("졌습니다.")
