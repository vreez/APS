import sys; sys.stdin = open("6030.txt", "r")

P, Q = map(int, input().split())
P_nums = []
Q_nums = []

for i in range(1, P+1):
    if P % i == 0:
        P_nums.append(i)
for j in range(1, Q+1):
    if Q % j == 0:
        Q_nums.append(j)

for i in range(len(P_nums)):
    for j in range(len(Q_nums)):
        print(P_nums[i], Q_nums[j])