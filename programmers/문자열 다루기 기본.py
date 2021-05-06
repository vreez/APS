s = '1234'
answer = True
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
if len(s) == 4 or len(s) == 6:
    for i in range(len(s)):
        if s[i] not in num:
            answer = False
else:
    answer = False

print(answer)
