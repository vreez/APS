import sys; sys.stdin = open("5945.txt", "r")

N = int(input())
if N > 50 or N % 2 == 0:
    print("INPUT ERROR!")
else:
    num = 0
    for i in range(1, N+1):
        num += i
        if i % 2 != 0:
            for j in range(num-i+1, num + 1):
                print(j, end=" ")
        else:
            for j in range(num, num-i, -1):
                print(j, end=" ")
        print()

