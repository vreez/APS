nums = list(map(int, input().split()))
cnt = 0
for i in range(10):
    if nums[i] % 2 == 0:
        cnt += 1

print("입력받은 짝수는 {}개입니다.".format(cnt))