# 계속 시간 초과가 나서 코드 참고 후 풀이

import sys; sys.stdin = open("10815.txt", "r")

N = int(input())
card = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

card_list = {}

for i in range(M):
    card_list[arr[i]] = 0

for num in range(N):
    if card[num] in card_list:
        card_list[card[num]] = 1

for value in card_list.values():
    print(value, end=' ')

