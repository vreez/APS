# import sys
# sys.stdin = open('input.txt')

for t in range(1, 11):
    T = int(input())
    numbers = list(map(int, input().split()))
    
    result = 0
    for i in range(len(numbers)):
        if (len(numbers)-1) > i > 1:
            if numbers[i] > numbers[i+1] and numbers[i] > numbers[i+2] and numbers[i] > numbers[i-1] and numbers[i] > numbers[i-2]:
                result += (numbers[i] - max(numbers[i-2], numbers[i-1], numbers[i+1], numbers[i+2]))
            else:
                result += 0    


    print('#{} {}'.format(t, result))