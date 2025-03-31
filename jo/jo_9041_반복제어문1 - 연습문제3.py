while True:
    print("점수를 입력하세요.", end=" ")
    N = int(input())
    if N < 0 or N > 100:
        break
    else:
        if N >= 80:
            print("축하합니다. 합격입니다.")
        else:
            print("죄송합니다. 불합격입니다.")

