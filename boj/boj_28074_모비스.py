import sys; sys.stdin = open("28074.txt", "r")

word = list(input())
if "M" in word and "O" in word and "B" in word and "I" in word and "S" in word:
    print("YES")
else:
    print("NO")

