from itertools import permutations

def solution(numbers):
    check = [True] * 10000000
    for i in range(2, int(9999999 ** 0.5) + 1):
        if check[i] == True:
            j = 2
            while i * j <= 9999999:
                check[i * j] = False
                j += 1
    answer = 0
    numbers = list(numbers)
    groups = []
    for i in range(1, len(numbers) + 1):
        groups += list(map(''.join, permutations(numbers, i)))
    groups = list(set(groups))
    count = 0
    checked = []
    for i in range(len(groups)):
        if int(groups[i]) >= 2 and int(groups[i]) not in checked:
            if check[int(groups[i])] == True:
                count += 1
                checked.append(int(groups[i]))

    answer = count
    return answer