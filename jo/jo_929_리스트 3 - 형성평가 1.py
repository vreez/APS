import sys; sys.stdin = open("929.txt","r")

n = int(input())
arr = []
for i in range(1, n+1):
    word = "No." + str(i)
    arr.append(word)
print(arr)