import sys; sys.stdin = open("9366.txt", "r")

T = int(input())
for i in range(T):
    arr = list(map(int, input().split()))
    new = sorted(arr)
    if new[0] + new[1] <= new[2]:
        print("Case #{}: {}".format(i+1, "invalid!"))
    else:
        if len(set(new)) == 1:
            print("Case #{}: {}".format(i + 1, "equilateral"))
        elif len(set(new)) == 2:
            print("Case #{}: {}".format(i + 1, "isosceles"))
        else:
            print("Case #{}: {}".format(i + 1, "scalene"))