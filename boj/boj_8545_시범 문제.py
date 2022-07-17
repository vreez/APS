import sys; sys.stdin = open("8545.txt", "r")

word = list(input())

new_word = word[::-1]

result = ''.join(map(str, new_word))

print(result)