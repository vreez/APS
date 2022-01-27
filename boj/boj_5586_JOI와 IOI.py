import sys; sys.stdin = open("5586.txt", "r")

words = list(input())
N = len(words)

JOI = 0
IOI = 0
for i in range(0, N-2):
    word = words[i:i+3]
    if "".join(word) == "JOI":
        JOI += 1
    elif "".join(word) == "IOI":
        IOI += 1
print(JOI)
print(IOI)