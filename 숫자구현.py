n = 8234
def big(n):
    num = list(str(n))
    if n >= 0:
        for i in range(len(num)):
            if int(num[i]) < 7:
                num[i] = '7' + num[i]
                break
            elif i == len(num)-1:
                num[i] = num[i] + '7'
    else:
        for i in range(1, len(num)):
            if int(num[i]) >= 7:
                num[i] = '7' + num[i]
                break
            elif i == len(num)-1:
                num[i] = num[i] + '7'
    return ''.join(num)

print(big(n))
