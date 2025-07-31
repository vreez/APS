a, b, c = map(int, input().split())

def func(x, y, z):
    avg = round((x+y+z) / 3, 2)
    print("세과목의 점수를 입력하세요.", end=" ")
    print("평균 : {:.2f}".format(avg))

func(a, b, c)