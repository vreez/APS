N = int(input())
for i in range(N):
    for j in range(N):
        print("({}, {})".format(i+1, j+1), end=" ")
    print()