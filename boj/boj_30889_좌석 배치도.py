import sys; sys.stdin = open("30889.txt", "r")

arr = [["."]*20 for _ in range(10)]
alpha = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5,
         "G":6, "H":7, "I":8, "J":9}
N = int(input())
for i in range(N):
    cus = input()
    one = alpha[cus[0]]
    two = int(cus[1:])-1
    arr[one][two] = "o"

for i in range(10):
    for j in range(20):
        print(arr[i][j], end="")
    print()

