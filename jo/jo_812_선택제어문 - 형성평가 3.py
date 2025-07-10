year = int(input())
result = "leap year" if year % 400 == 0 else("leap year" if year % 4 == 0 and year % 100 != 0 else "common year")
print(result)