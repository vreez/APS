arr = []
print("단어 5개를 입력하세요.")
for i in range(5):
    arr.append(input())

new = sorted(arr)
for i in range(5):
    print(new[i])