import sys; sys.stdin = open("5201.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    my_container = sorted(container, reverse=True)
    my_truck = sorted(truck, reverse=True)

    count = 0

    extra = 0
    for i in range(M):
        if i < N:
            if my_container[i] > max(my_truck):
                extra -= 1
            elif my_container[i] <= my_truck[i + extra]:
                count += my_container[i]
            elif my_container[i] > my_truck[i + extra]:
                extra -= 1
                continue

    print("#{} {}".format(tc, count))

