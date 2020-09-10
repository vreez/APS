# 이진힙을 구현할 수 있으면 풀 수 있는 문제이다.

'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''

def heappush(a):
    global hsize
    hsize += 1
    H[hsize] = a
    c, p = hsize, hsize//2
    while p:
        if H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c = p
            p = c // 2
        else:
            break

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    H = [0] * (N+1)
    hsize = 0

    for i in range(N):
        heappush(arr[i])

    total = 0
    for j in range(1, N+1):
        while N//2:
            total += H[N//2]
            N = N//2

    # print(H)
    print('#{} {}'.format(tc, total))


