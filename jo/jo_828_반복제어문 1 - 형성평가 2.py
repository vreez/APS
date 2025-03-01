import sys; sys.stdin = open("828.txt", "r")

odd = 0
even = 0
while True:
    N = int(input())
    if N == 0:
        break
    else:
        if N % 2 == 0:
            even += 1
        else:
            odd += 1

print("odd : {}".format(odd))
print("even : {}".format(even))
