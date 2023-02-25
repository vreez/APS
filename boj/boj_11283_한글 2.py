import sys; sys.stdin = open("11283.txt", "r")

word = input()
print(ord(word) - ord('가')+1)