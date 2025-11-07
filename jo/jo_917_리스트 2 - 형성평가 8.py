words = ["flower", "rose", "lily", "daffodil", "azalea"]
alpha = input()
count = 0
ans = []
for word in words:
    if word[1] == alpha or word[2] == alpha:
        ans.append(word)
        count += 1
if len(ans) > 0:
    for a in ans:
        print(a)
print(count)
