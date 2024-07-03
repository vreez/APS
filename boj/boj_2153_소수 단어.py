import sys; sys.stdin = open("2153.txt", "r")

arr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
word = input()
total = 0
for i in range(len(word)):
    total += (arr.find(word[i]) + 1)
check = True
if total != 1:
    for j in range(2, int(total**0.5)+1):
        if total % j == 0:
            check = False

if check == True:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
