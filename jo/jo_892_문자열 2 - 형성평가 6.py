word = input()
lower = 0
upper = 0
digit = 0
for i in range(len(word)):
    if word[i].islower():
        lower += 1
    if word[i].isupper():
        upper += 1
    if word[i].isdigit():
        digit += 1
if len(word) == upper:
    print("U")
elif len(word) == lower:
    print("L")
elif len(word) == digit:
    print("D")
else:
    print("X")

print(word.upper())