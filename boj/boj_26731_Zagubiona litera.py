import sys; sys.stdin = open("26731.txt", "r")

arr = list(input())
new = sorted(arr)

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']

answer = list(set(alpha) - set(new))
print(answer[0])

