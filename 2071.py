T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))

    results = 0
    count = 0

    for number in numbers:
        results += number
        count += 1
    
    result = int(round(results/count, 0))

    print('#{} {}'.format(t, result))