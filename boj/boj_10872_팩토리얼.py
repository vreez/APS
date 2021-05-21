import sys; sys.stdin = open("10872.txt")

N = int(input())

def factorial(N):
    # N이 1보다 같거나 작으면 무조건 1을 return해야 한다. 안그러면 런타임에러가 발생한다.
    if N <= 1:
        return 1
    else:
        return N * factorial(N-1)

print(factorial(N))