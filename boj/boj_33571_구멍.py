arr = list(input())
ans = 0
for a in arr:
    if a == "A" or a == "a" or a == "b" or a == "D" or a == "d" or a == "e" or a == "g" or a == "O" or a == "o" or a == "P" or a == "p" or a == "Q" or a == "q" or a == "R" or a == "@":
        ans += 1
    elif a == "B":
        ans += 2
print(ans)