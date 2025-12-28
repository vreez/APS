N = int(input())
cnt = 0
for i in range(N):
    word = input()
    if word[0] == "C":
        cnt += 1
print(cnt)