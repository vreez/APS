nums = list(map(int, input().split()))
even = 0
odd = 0
for i in range(10):
    if nums[i] % 2 == 0:
        even += 1
    else:
        odd += 1
print("even : {}".format(even))
print("odd : {}".format(odd))