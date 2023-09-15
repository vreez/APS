import sys; sys.stdin = open("1076.txt", "r")

color = ["black", "brown", "red", "orange", "yellow", "green", "blue",
         "violet", "grey", "white"]
one = input()
two = input()
three = input()

total = (color.index(one)*10 + color.index(two))*(10**color.index(three))
print(total)
