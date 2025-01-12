import sys; sys.stdin = open("9596.txt", "r")

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(1, 5):
    print("피보나치 수열 {}항 : {}".format(i*10, fibo(i*10)))