import sys; sys.stdin = open("18301.txt", "r")

n1, n2, n3 = map(int, input().split())

result = ((n1 + 1) * (n2 + 1) // (n3 + 1)) - 1
print(result)