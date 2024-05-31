import sys; sys.stdin = open("26535.txt", "r")
import math

num = int(input())
s = math.ceil(math.sqrt(num))

print("x"*(s+2))
for i in range(s):
    print("x"+"."*s+"x")
print("x"*(s+2))
