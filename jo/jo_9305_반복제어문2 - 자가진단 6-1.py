N = int(input())
two = 0
three = 0
for i in range(N):
    num = int(input())
    if num % 2 == 0:
        two += 1
    if num % 3 == 0:
        three += 1
print("2의 배수: {}".format(two))
print("3의 배수: {}".format(three))