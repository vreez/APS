one = list(map(int, input().split()))
two = list(map(int, input().split()))
three = list(map(int, input().split()))
four = list(map(int, input().split()))
five = list(map(int, input().split()))

cnt = 0
if sum(one)/4 >= 80:
    cnt += 1
    print("pass")
else:
    print("fail")
if sum(two)/4 >= 80:
    cnt += 1
    print("pass")
else:
    print("fail")
if sum(three)/4 >= 80:
    cnt += 1
    print("pass")
else:
    print("fail")
if sum(four)/4 >= 80:
    cnt += 1
    print("pass")
else:
    print("fail")
if sum(five)/4 >= 80:
    cnt += 1
    print("pass")
else:
    print("fail")
print("Successful : {}".format(cnt))