def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x:x*3, reverse = True)
    if int(''.join(numbers)) == 0:
        answer = '0'
    else:
        answer = ''.join(numbers)
    return answer