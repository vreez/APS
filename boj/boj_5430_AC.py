import sys; sys.stdin = open("5430.txt", "r")

T = int(input())
for _ in range(T):
    p = list(input())
    n = int(input())
    arr = input().strip('[]').split(',')
    isError = False
    isReverse = False

    if len(arr) == 1 and arr[0] == '':
        arr = []

    if isError == False:
        for order in p:
            if order == 'R':
                isReverse = not isReverse
            else:
                if len(arr) == 0:
                    isError = True
                else:
                    if isReverse:
                        arr.pop(-1)
                    else:
                        arr.pop(0)

    if isError == False:
        if len(arr) != 0:
            result = '['
            if isReverse:
                for i in range(len(arr)-1, -1, -1):
                    if i != 0:
                        result += (arr[i] + ',')
                    else:
                        result += (arr[i] + ']')
            else:
                for i in range(len(arr)):
                    if i != len(arr) - 1:
                        result += (arr[i] + ',')
                    else:
                        result += (arr[i] + ']')
        else:
            result = arr
    if isError:
        result = 'error'

    print(result)
