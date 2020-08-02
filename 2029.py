T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    
    quotient = numbers[0] // numbers[1]
    remainder = numbers[0] % numbers[1]
            
    print('#{} {} {}'.format(t, quotient, remainder))