dic = {}

while True:
    name = input()
    if name in dic:
        print("이름은?", end=" ")
        print("{}의 별명은 {}입니다^^".format(name, dic[name]))
        break
    else:
        nickname = input()
        dic[name] = nickname
        print("이름은?", end=" ")
        print("{}의 별명은?".format(name), end=" ")
        print("===============")
