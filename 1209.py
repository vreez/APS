# import sys
# sys.stdin = open('1209.txt')

for t in range(1, 11):
    my_numbers = []
    T = int(input())
    for a in range(100):
        numbers = list(map(int, input().split()))
        my_numbers.append(numbers)

        N = len(my_numbers)
        M = len(my_numbers[0])

        my_row_sum = []
        for i in my_numbers:
            my_sum = 0
            for j in i:
                my_sum += j  
            my_row_sum += [my_sum]   

        my_column_sum = []
        for j in range(M):
            my_sum2 = 0
            for i in range(N):
                my_sum2 += my_numbers[i][j]
            my_column_sum.append(my_sum2)

        my_sum3 = 0
        for m in range(N):
            for n in range(M):
                if m == n:
                    my_sum3 += my_numbers[m][n]   

        my_sum4 = 0
        for m in range(N):
            for n in range(M):
                if m + n == 99:
                    my_sum4 += my_numbers[m][n]   

        all_in_one = my_row_sum + my_column_sum + [my_sum3] + [my_sum4]

        max_size = 0
        for o in all_in_one:
            if o > max_size:
                max_size = o
        
    print('#{} {}'.format(t, max_size))       



