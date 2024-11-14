import sys; sys.stdin = open("518.txt", "r")

arr = list(map(int, input().split()))
print("sum : {}".format(sum(arr)))
print("avg : {}".format(sum(arr)//3))