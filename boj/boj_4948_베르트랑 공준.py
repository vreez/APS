# 에라토스테네스의 체 알고리즘 활용
import sys; sys.stdin = open("input/4948.txt", "r")
import math;

while True:
    n = int(input())
    if n == 0:
        break

    arr = [True for i in range((2 * n) + 1)]
    # 자연수의 경우, 가운데 약수를 기준으로 각 등식이 대칭적인 형태를 보이므로
    # 여기서는 2 * n의 제곱근까지만 확인하면 된다.
    for i in range(2, int(math.sqrt(2 * n)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= 2 * n:
                arr[i * j] = False
                j += 1

    count = 0
    for i in range(n + 1, (2 * n) + 1):
        if i > 1 and arr[i] == True:
            count += 1

    print(count)
