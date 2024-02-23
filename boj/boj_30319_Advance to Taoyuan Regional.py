import sys; sys.stdin = open("30319.txt", "r")
from datetime import datetime

contest = datetime.strptime(input(), "%Y-%m-%d")
target = datetime.strptime("2023-10-21", "%Y-%m-%d")
day = target - contest

if int(day.days) >= 35:
    print("GOOD")
else:
    print("TOO LATE")