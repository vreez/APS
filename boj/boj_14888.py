'''
5
100 100 100 100 10
0 0 4 0
'''
T = int(input())
numbers = list(map(int, input().split()))
my_list = list(map(int, input().split()))
arr = []
for i in range(4):
    if my_list[i] != 0:
        for j in range(my_list[i]):
            if i == 0:
                arr.append('+')
            elif i == 1:
                arr.append('-')
            elif i == 2:
                arr.append('*')
            else:
                arr.append('//')

N = T - 1
result = []
max_num = -1000000000
min_num = 1000000000
def perm(k):
    global max_num, min_num
    if k == N:
        new_number = numbers.copy()
        # print(arr)
        for n in range(N):
            if arr[n] == '+':
                new_number.insert(0, new_number.pop(0) + new_number.pop(0))
            elif arr[n] == '-':
                new_number.insert(0, new_number.pop(0) - new_number.pop(0))
            elif arr[n] == '*':
                new_number.insert(0, new_number.pop(0) * new_number.pop(0))
            else:
                if new_number[0] >= 0:
                    new_number.insert(0, new_number.pop(0) // new_number.pop(0))
                else:
                    new_number.insert(0, -(-(new_number.pop(0)) // new_number.pop(0)))
        # result.append(new_number)
        if new_number[0] >= max_num:
            max_num = new_number[0]
        if new_number[0] <= min_num:
            min_num = new_number[0]

    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k+1)
            arr[k], arr[i] = arr[i], arr[k]

perm(0)

print(max_num)
print(min_num)



