s, e = map(int, input().split())

# s와 e가 구구단의 범위를 넘어갔을 때
if s > 9 or e > 9 or s < 2 or e < 2:
    # s와 e가 구구단의 범위에 속할 때까지 계속해서 input error를 발생시키고 새로운 s, e을 받는다.
    while s > 9 or e > 9 or s < 2 or e < 2:
        print("INPUT ERROR!")
        s, e = map(int, input().split())
    # s와 e값이 구구단의 범위에 만족하게 되었을 때, 구구단을 출력한다.
    # s값이 3값보다 크거나 같을 경우
    if s >= e:
        for i in range(1, 10):
            for j in range(s, e-1, -1):
                if j * i < 10:
                    # 구구단의 결과가 한 자리 수일 때, 공백을 더해 자리수를 맞춰준다.
                    print("{} * {} = {}{}".format(j, i, " ", j * i), end="   ")
                else:
                    print("{} * {} = {}".format(j, i, j * i), end="   ")
            print()
    # s값이 e값 보다 작을 경우
    else:
        for i in range(1, 10):
            for j in range(s, e+1):
                if j * i < 10:
                    print("{} * {} = {}{}".format(j, i, " ", j * i), end="   ")
                else:
                    print("{} * {} = {}".format(j, i, j * i), end="   ")
            print()
# s와 e가 구구단의 범위 안에 속할 때
else:
    # s값이 e값 보다 크거나 같을 경우
    if s >= e:
        for i in range(1, 10):
            for j in range(s, e-1, -1):
                if j * i < 10:
                    print("{} * {} = {}{}".format(j, i, " ", j * i), end="   ")
                else:
                    print("{} * {} = {}".format(j, i, j * i), end="   ")
            print()
    # s값이 e값보다 작을 경우
    else:
        for i in range(1, 10):
            for j in range(s, e+1):
                if j * i < 10:
                    print("{} * {} = {}{}".format(j, i, " ", j * i), end="   ")
                else:
                    print("{} * {} = {}".format(j, i, j * i), end="   ")
            print()
