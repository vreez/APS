cnt = 0
ans = []
while True:
    word = input()
    if word == "0":
        break
    else:
        cnt += 1
        if "mo" in word:
            ans.append(word)
print(cnt)
for a in ans:
    print(a)

