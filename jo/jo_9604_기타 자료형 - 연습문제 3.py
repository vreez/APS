import sys; sys.stdin = open("9604.txt", "r")
n = int(input())
tp = ()
print("학생은 몇 명?", end=" ")
for i in range(6):
    print("이름 나이 사용언어?", end=" ")
for i in range(6):
    tp += tuple(input().split())

for i in range(3*n):
     if tp[i] == "Python" and int(tp[i-1]) <= 19:
         print(tp[i-2])

