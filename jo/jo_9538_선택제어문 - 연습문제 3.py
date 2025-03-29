import sys; sys.stdin = open("9538.txt", "r")

N = int(input())
print("점수를 입력하세요.", end=" ")

if N >= 80:
    print("축하합니다. 합격입니다.")
else:
    print("불합격입니다.")
