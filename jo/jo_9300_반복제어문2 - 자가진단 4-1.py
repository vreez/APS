S, E = map(int, input().split())

if S % 2 == 0:
    for i in range(S-1, E-1,-2):
        print(i)
else:
    for i in range(S, E-1, -2):
        print(i)