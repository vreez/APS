N = int(input())
arr = []
for i in range(N):
    sen = input()
    arr.append(sen)
for s in arr[::-1]:
    print(s)