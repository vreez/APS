print("세 수를 입력하세요.", end=" ")
nums = list(map(int, input().split()))
print("입력받은 수중 가장 큰 수는 {}입니다.".format(max(nums)))