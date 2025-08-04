a, b = map(int, input().split())

def func(m, n):
    print("두 수를 입력하세요.", end=" ")
    print("첫 번째 함수 실행중 a = {}, b = {}".format(n, m))
    print("첫 번째 함수 실행후 a = {}, b = {}".format(m, n))
    print("두 번째 함수 실행중 a = {}, b = {}".format(n, m))
    print("두 번째 함수 실행후 a = {}, b = {}".format(n, m))

func(a, b)
