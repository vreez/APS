# T = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
T = str(input())

result = ''

for i in T:
    result += str(ord(i)-64) + ' '

print(result)    




  