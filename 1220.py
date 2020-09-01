import sys
sys.stdin = open("1220.txt")

for tc in range(1, 11):
    input()
    table = [list(map(int, input().split())) for _ in range(100)]

    total = []

    for i in range(100):
        mag = []
        for j in range(100):
            if table[j][i] != 0:
                mag.append(table[j][i])

        count = 0
        for n in range(len(mag)):
            if n < len(mag)-1:
                if mag[n] == 1 and mag[n+1] == 2:
                    count += 1
        total.append(count)

    my_total = 0
    for k in range(len(total)):
        my_total += total[k]

    print("#{} {}".format(tc, my_total))

