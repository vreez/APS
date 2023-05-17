import sys; sys.stdin = open("25785.txt", "r")

word = list(input())
check = True
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(1, len(word)):
    if word[i-1] not in vowels:
        if word[i] in vowels:
            check = True
        else:
            check = False
            break
    else:
        if word[i] not in vowels:
            check = True
        else:
            check = False
            break

if check == True:
    print(1)
else:
    print(0)
