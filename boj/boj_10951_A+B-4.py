import sys; sys.stdin = open("10951.txt", "r")

while True:
    try:
        A, B = sys.stdin.readline().split()
        print(int(A) + int(B))
    except:
        break