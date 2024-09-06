import sys; sys.stdin = open("17285.txt", "r")

arr = input()
key = ord(arr[0])^ord("C")
for i in arr:
    new = chr(ord(i)^ key)
    print(new, end="")