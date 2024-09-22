import sys; sys.stdin = open("32306.txt", "r")

team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

total1 = team1[0] + (team1[1] * 2) + (team1[2] * 3)
total2 = team2[0] + (team2[1] * 2) + (team2[2] * 3)

if total1 > total2:
    print(1)
elif total2 > total1:
    print(2)
else:
    print(0)