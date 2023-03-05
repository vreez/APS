import sys; sys.stdin = open("27257.txt", "r")

num = input()
new_f = num.rstrip("0")
new_s = new_f[1:]

count = 0
for i in range(len(new_s)):
    if new_s[i] == "0":
        count += 1

print(count)
        