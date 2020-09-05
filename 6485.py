T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_line = []
    for bus in range(N):
        a, b = map(int, input().split())
        bus_line.append([a,b])
    # print(bus_line)
    P = int(input())
    bus_stops =[]
    for bus_stop in range(P):
        bus_stops.append(int(input()))

    count = [0] * 5001

    for line in range(len(bus_line)):
        for i in range(bus_line[line][0], bus_line[line][1]+1):
            count[i] += 1
    # print(count)
    my_result = []
    for j in range(len(bus_stops)):
        my_result.append(count[bus_stops[j]])

    print("#{}".format(tc), end=" ")
    for j in range(len(my_result)):
        print("{}".format(my_result[j]), end=" ")
    print()