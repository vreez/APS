import sys; sys.stdin = open("5946.txt", "r")

n = int(input())
if n > 50 or n % 2 == 0:
    print("INPUT ERROR!")
else:
    for i in range(n):
        print(" "*(i*2) + (str(i)+" ")*(2*(n-i)-1))