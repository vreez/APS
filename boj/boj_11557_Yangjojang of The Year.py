import sys; sys.stdin = open("11557.txt", "r")

T = int(input())
for _ in range(T):
    N = int(input())
    school = ''
    consum = 0
    for i in range(N):
        name, consumption = input().split()
        if consum < int(consumption):
            consum = int(consumption)
            school = name

    print(school)