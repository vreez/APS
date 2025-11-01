words = []
for i in range(10):
    word = input()
    words.append(word)

spell = input()

new = []
for i in range(10):
    if spell in words[i]:
        new.append(words[i])

new = sorted(new)

for i in range(len(new)):
    print(new[i])
