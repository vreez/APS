one = list(map(int, input().split()))
two = list(map(int, input().split()))
three = list(map(int, input().split()))
four = list(map(int, input().split()))


print("1class? 2class? 3class? 4class?", end=" ")
print("1class : {}".format(sum(one)))
print("2class : {}".format(sum(two)))
print("3class : {}".format(sum(three)))
print("4class : {}".format(sum(four)))