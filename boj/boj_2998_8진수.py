import sys; sys.stdin = open("2998.txt", "r")

num = input()
n = len(num)
if n % 3 != 0:
    num = '0' * (3 - (n % 3)) + num
ans = ""
for i in range(0, len(num), 3):
    new = num[i:i+3]
    if new == "000":
        ans += "0"
    elif new == "001":
        ans += "1"
    elif new == "010":
        ans += "2"
    elif new == "011":
        ans += "3"
    elif new == "100":
        ans += "4"
    elif new == "101":
        ans += "5"
    elif new == "110":
        ans += "6"
    elif new == "111":
        ans += "7"

print(ans)