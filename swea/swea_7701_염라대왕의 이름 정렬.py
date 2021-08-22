import sys; sys.stdin = open("7701.txt", "r")

T = int(input())
for i in range(T):
    N = int(input())
    arr = list(input() for _ in range(N))
    arr = list(set(arr))
    result = sorted(arr, key= lambda x : (len(x), x))
    print('#{}'.format(i + 1))
    for item in result:
        print(item)