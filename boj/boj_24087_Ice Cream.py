import sys; sys.stdin = open("24087.txt", "r")

S = int(input())
A = int(input())
B = int(input())

if S >= A:
    num = (S - A) // B

    if ((S - A) % B) > 0 and (S - A) != 0:
        num += 1
    answer = 250 + (100 * num)
else:
    answer = 250
print(answer)