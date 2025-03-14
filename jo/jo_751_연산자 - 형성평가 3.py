import sys; sys.stdin = open("751.txt", "r")

a = int(input())
b = int(input())
newA = a + 5
newB = b * 2
print("width = {}".format(newA))
print("length = {}".format(newB))
print("area = {}".format(newA*newB))