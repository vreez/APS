def func(li):
    total = 0
    for i in range(5):
        total += abs(li[i])
    print(total)

li = list(map(int, input().split()))
func(li)