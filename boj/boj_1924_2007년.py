import sys; sys.stdin = open("1924.txt", "r")

M, D = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

result = (sum(month[:M-1]) + D) % 7

days = {
    0:'SUN', 1:'MON', 2:'TUE', 3:'WED',
    4:'THU', 5:'FRI', 6:'SAT'
}

print(days[result])