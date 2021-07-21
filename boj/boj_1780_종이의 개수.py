import sys; sys.stdin = open("input/1780.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = {-1: 0, 0: 0, 1: 0}

def check(col, row, N):
    count = 0
    for i in range(col, col + N):
        for j in range(row, row + N):
            if arr[i][j] == arr[col][row]:
                count += 1
    if N * N == count:
        result[arr[col][row]] += 1
    else:
        check(col, row, N // 3)
        check(col, row + N // 3, N // 3)
        check(col, row + N // 3 * 2, N // 3)
        check(col + N // 3, row, N // 3)
        check(col + N // 3, row + N // 3, N // 3)
        check(col + N // 3, row + N // 3 * 2, N // 3)
        check(col + N // 3 * 2, row, N // 3)
        check(col + N // 3 * 2, row + N // 3, N // 3)
        check(col + N // 3 * 2, row + N // 3 * 2, N // 3)

    return result

check(0, 0, N)


print(result[-1])
print(result[0])
print(result[1])