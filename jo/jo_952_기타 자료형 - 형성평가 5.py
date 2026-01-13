n = int(input())
dic = {}

for i in range(n):
    a, b = input().split()
    dic[a] = b
word = input()
print(dic[word])
