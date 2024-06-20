import sys; sys.stdin = open("2948.txt", "r")
import datetime

D, M = map(int, input().split())
check = datetime.date(2009, M, D).weekday()
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(week[check])
