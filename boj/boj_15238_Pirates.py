import sys; sys.stdin = open("15238.txt", "r")

dict = {}
N = int(input())
arr = list(input())

for chr in arr:
    if chr in dict:
        dict[chr] += 1
    else:
        dict[chr] = 1

alpha = max(dict, key=dict.get)
num = max(dict.values())

print(alpha, num)
