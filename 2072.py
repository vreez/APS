T = int(input())

for t in range(1, T+1):
    # 3 17 1 39 8 41 2 32 99 2
    numbers = list(map(float, input().split()))
    
    result = 0
    for number in numbers:
        if number % 2:
            result += number       
            
    print('#{} {}'.format(t, result))