import sys; sys.stdin = open("28431.txt", "r")

check = [0]*10
for i in range(5):
    s = int(input())
    check[s] += 1

for i in range(10):
    if check[i] % 2 == 1:
        print(i)
