arr = []

for i in range(3):
    scores = list(map(int, input().split()))
    arr.append(scores)

def func(arr):
    total1 = 0
    total2 = 0
    total3 =0
    for i in range(3):
        for j in range(3):
            print(arr[i][j], end=" ")
            if j == 0:
                total1 += arr[i][j]
            elif j == 1:
                total2 += arr[i][j]
            else:
                total3 += arr[i][j]
        print(sum(arr[i]))
    print("{} {} {} {}".format(total1, total2, total3, total1+total2+total3))

func(arr)