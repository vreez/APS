import sys; sys.stdin = open("2869.txt", "r")

A, B, V = map(int, input().split())

# day = 0
# while V > 0:
#     V -= A
#     if V > 0:
#         V += B
#     day += 1
# print(day)

day = (V-A) // (A-B)
# V와 A가 같을 경우 소요시간은 무조건 1일이다.
if V == A:
    day = 1
elif day < 1:
    day += 2
else:
    # (V-A) % (A-B)를 했을 때 나머지가 나올 경우, 1일이 더 소요된다. ex) 4 2 17
    if (V-A) % (A-B) > 0:
        day += 2
    else:
        day += 1
print(day)





