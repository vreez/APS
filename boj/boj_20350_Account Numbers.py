import sys; sys.stdin = open("20350.txt", "r")

arr = list(input())
new = arr[4:] + arr[:4]
num = ""
for i in range(len(new)):
    if new[i].isalpha():
        num += str(ord(new[i]) - 55)
    else:
        num += new[i]

ans = int(num)
if ans % 97 == 1:
    print("correct")
else:
    print("incorrect")