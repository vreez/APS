import sys; sys.stdin = open("1042.txt", "r")

N = int(input())

a = input()
b = input()

first = int(a, N) + int(b, N)

second = ''
while first:
    ans = first % N
    if ans >= 10:
        if ans == 10:
            ans = "A"
        elif ans == 11:
            ans = "B"
        elif ans == 12:
            ans = "C"
        elif ans == 13:
            ans = "D"
        elif ans == 14:
            ans = "E"
        else:
            ans = "F"
    second += str(ans)
    first //= N
print(int(a, N) + int(b, N))
print(second[::-1])
