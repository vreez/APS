import sys; sys.stdin = open("1919.txt", "r")

first = input()
second = input()

f_word = []
f_num = []
s_word = []
s_num = []
for i in range(len(first)):
    if first[i] not in f_word:
        f_word.append(first[i])
        f_num.append(first.count(first[i]))
for j in range(len(second)):
    if second[j] not in s_word:
        s_word.append(second[j])
        s_num.append(second.count(second[j]))
total = 0
for i in range(len(f_word)):
    if f_word[i] not in s_word:
        total += f_num[i]
    else:
        if f_num[i] > s_num[s_word.index(f_word[i])]:
            total += (f_num[i] - s_num[s_word.index(f_word[i])])
for i in range(len(s_word)):
    if s_word[i] not in f_word:
        total += s_num[i]
    else:
        if s_num[i] > f_num[f_word.index(s_word[i])]:
            total += (s_num[i] - f_num[f_word.index(s_word[i])])

print(total)