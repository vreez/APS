a = int(input())
b, c = map(int, input().split())
def func(a, b, c):
    print("정사각형의 넓이 :", end=" ")
    print("정사각형의 한 변의 길이 : {:.6f}".format(a**0.5))
    print("밑과 지수 :", end=" ")
    print("{:.6f}의 {:.6f}승은 {:.6f}입니다.".format(b, c, b**c))

func(a, b, c)
