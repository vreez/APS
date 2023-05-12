import sys; sys.stdin = open("21185.txt", "r")

N = int(input())

first = 0
for i in range(5, 5+N):
    first += i
second = 0
for j in range(6, 6+N):
    second += j

if first % 2 and second % 2:
    print("Odd")
elif first % 2 == 0 and second % 2 == 0:
    print("Even")
else:
    print("Either")
