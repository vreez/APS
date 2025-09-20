cnt = 0
def pri(cnt, n):
    if cnt >= n:
        return
    else:
        print("recursive")
        cnt += 1
        pri(cnt, n)
n = int(input())
pri(cnt, n)