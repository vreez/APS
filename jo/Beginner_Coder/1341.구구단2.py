s, e = map(int, input().split())

# s가 e보다 크거나 같을 경우
if s >= e:
    for i in range(s, e-1, -1):
        # 3개씩 끊어서 출력해야 하므로
        for j in range(1, 9, 3):
            # 새로운 k라는 변수를 사용하여 값을 1씩 증가시키고 한 줄에 3개의 구구단이 작성되면 while문 탈출
            k = j
            while k < j + 3:
                if i * k < 10:
                    print("{} * {} = {}{}".format(i, k, " ", i * k), end="   ")
                else:
                    print("{} * {} = {}".format(i, k, i * k), end="   ")
                k += 1
            print()
        # 구구단의 각 단 사이는 한 줄 비워둔다.
        print()
# s가 e보다 작을 경우
else:
    for i in range(s, e+1):
        for j in range(1, 9, 3):
            k = j
            while k < j + 3:
                if i * k < 10:
                    print("{} * {} = {}{}".format(i, k, " ", i * k), end="   ")
                else:
                    print("{} * {} = {}".format(i, k, i * k), end="   ")
                k += 1
            print()
        print()