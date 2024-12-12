import sys; sys.stdin = open("9589.txt", "r")

arr = list(map(int, input().split()))
total = sum(arr)
avg = round(total/10, 1)
print("총점 = {}".format(total))
print("평균 = {}".format(avg))