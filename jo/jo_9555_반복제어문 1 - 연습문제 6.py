import sys; sys.stdin = open("9555.txt", "r")

while True:
    N = int(input())
    if N == 4:
        print("1. 입력하기")
        print("2. 출력하기")
        print("3. 삭제하기")
        print("4. 끝내기")
        print("작업할 번호를 선택하세요.")
        print()
        print("끝내기를 선택하였습니다.")
        break
    else:
        print("1. 입력하기")
        print("2. 출력하기")
        print("3. 삭제하기")
        print("4. 끝내기")
        print("작업할 번호를 선택하세요.")
        print()
        if N == 1:
            print("입력하기를 선택하였습니다.")
        elif N == 2:
            print("출력하기를 선택하였습니다.")
        elif N == 3:
            print("삭제하기를 선택하였습니다.")
        else:
            print("잘못 선택하였습니다.")
        print()