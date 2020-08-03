T = int(input())

for t in range(1, T+1):
    numbers = int(input())
    
    result = 0
    for number in range(1, numbers + 1):
        if number % 2:
            result += number
        else:
            result -= number    

    print('#{} {}'.format(t, result))