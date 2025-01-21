while True:
    print("점수를 입력하세요.", end=" ")
    num = int(input())
    if num < 0 or num > 100:
        break
    else:
        if num >= 80:
            print("축하합니다. 합격입니다.")
        else:
            print("죄송합니다. 불합격입니다.")