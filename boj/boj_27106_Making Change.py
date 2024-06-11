import sys; sys.stdin = open("27106.txt", "r")

P = int(input())
change = 100-P
print(change // 25, end=" ")
change %= 25
print(change // 10, end=" ")
change %= 10
print(change // 5, end=" ")
change %= 5
print(change)
