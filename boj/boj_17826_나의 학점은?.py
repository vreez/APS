import sys; sys.stdin = open("17826.txt", "r")

arr = list(map(int, input().split()))
new = sorted(arr)[::-1]
score = int(input())
rank = new.index(score) + 1

if rank <= 5:
    print("A+")
elif rank <= 15:
    print("A0")
elif rank <= 30:
    print("B+")
elif rank <= 35:
    print("B0")
elif rank <= 45:
    print("C+")
elif rank <= 48:
    print("C0")
else:
    print("F")
