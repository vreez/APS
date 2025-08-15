scores = list(map(int, input().split()))

def func(scores):
    print("3과목의 점수를 입력하세요.", end=" ")
    if sum(scores) // 3 < 60 or min(scores) < 40:
        print("불합격")
    else:
        print("축하합니다. 합격입니다.")

func(scores)