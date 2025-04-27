nums = list(map(int, input().split()))
th = 0
fi = 0
for i in range(10):
    if nums[i] % 3 == 0:
        th += 1
    if nums[i] % 5 == 0:
        fi += 1
print("Multiples of 3 : {}".format(th))
print("Multiples of 5 : {}".format(fi))