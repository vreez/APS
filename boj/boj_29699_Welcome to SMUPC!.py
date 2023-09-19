import sys; sys.stdin = open("29699.txt", "r")

N = int(input())
word = "WelcomeToSMUPC"
new = word*N
print(new[N-1])