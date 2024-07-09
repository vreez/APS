import sys; sys.stdin = open("26509.txt", "r")

T = int(input())
for i in range(T):
    first = sorted(list(map(int, input().split())))
    second = sorted(list(map(int, input().split())))
    if first == second and second[0]**2 + second[1]**2 == second[2]**2:
        print("YES")
    else:
        print("NO")