import sys; sys.stdin = open("27130.txt", "r")

one = int(input())
two = input()
print(one)
print(int(two))
for i in range(len(two)):
    print(one * int(two[len(two)-1-i]))
print(one * int(two))
