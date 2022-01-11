import sys; sys.stdin = open("5543.txt", "r")


burger = []
first = int(input())
second = int(input())
third = int(input())
burger.append(first)
burger.append(second)
burger.append(third)

beverage = []
cola = int(input())
cider = int(input())
beverage.append(cola)
beverage.append(cider)

print(min(burger) + min(beverage) - 50)

