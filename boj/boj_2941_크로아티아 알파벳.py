import sys; sys.stdin = open("input/2941.txt", "r")

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

count = 0

for i in range(len(croatia)):
    if croatia[i] in word:
        count += word.count(croatia[i])
        word = word.replace(croatia[i], '*')

for i in range(len(word)):
    if word[i] != '*':
        count += 1

print(count)

