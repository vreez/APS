import sys; sys.stdin = open("919.txt", "r")

words = []
for _ in range(5):
    words.append(input())
inputs = input().split()
if len(inputs) == 2:
    alpha, word = inputs
else:
    alpha = inputs[0]
    word = input()

ans = []
for w in words:
    if (alpha in w) or (word in w):
        ans.append(w)

if len(ans) > 0:
    for a in ans:
        print(a)
else:
    print("none")