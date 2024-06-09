import sys; sys.stdin = open("16172.txt", "r")

word = input()
fd = input()
ans = "".join(list(w for w in word if w.isalpha()))
print(1 if fd in ans else 0)
