import sys; sys.stdin = open("28249.txt", "r")

li = {"Poblano":1500, "Mirasol":6000, "Serrano":15500,
      "Cayenne":40000, "Thai":75000, "Habanero":125000}

N = int(input())
total = 0
for i in range(N):
    word = input()
    total += li[word]

print(total)