import sys
sys.stdin = open('input_data/2056.txt')

def check_month(month):
    # month = '02'
    if 0 < int(month) < 13:
        return month
    return ''

def check_day(month, day):
    # day = '28' , month = '02
    # key - month, value - day
    day_dict = {
        '01':31, '02':28,
        '03':31, '04':30,
        '05':31, '06':30,
        '07':31, '08':31,
        '09':30, '10':31,
        '11':30, '12':31,
    }
    # print(month, day)
    # print(day_dict.get(month))

    # '00'과 같은 dict에 없는 숫자가 있을 때는 none값이 나오므로
    if not day_dict.get(month):
        return ''

    if 0 < int(day) <= day_dict.get(month):
        # key로 value를 가져오자.
        return day
    return ''    

# '5' -> 5
T = int(input())

# 1, 2, 3, 4, 5
for t in range(1, T+1):
    # '22220228'
    target = input()

    year, month, day = target[:4], target[4:6], target[6:]
    # print(year, month, day)

    month = check_month(month)
    day = check_day(month, day)
    
    if month and day:
        print('#{} {}/{}/{}'.format(t, year, month, day))
    else:
        print('#{} -1'.format(t))   
