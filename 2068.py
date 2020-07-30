T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    
    max_size = 0
    for number in numbers:
        if number > max_size:
            max_size = number

    result = max_size         

    print('#{} {}'.format(t, result))