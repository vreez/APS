a, b = input().split()

if ord(a) <= ord(b):
    for i in range(ord(a), ord(b)+1):
        print(chr(i), end=" ")
else:
    for i in range(ord(a), ord(b)-1, -1):
        print(chr(i), end=" ")