arr = []
for i in range(5):
    money = int(input())
    arr.append(money)

print("1번 저축금액은? 2번 저축금액은? 3번 저축금액은? 4번 저축금액은? 5번 저축금액은? ", end="")
print("저축왕 {}번 {}원".format(arr.index(max(arr))+1, max(arr)))
