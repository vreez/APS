b = int(input())
flag = False
for i in range(3):
    if int(input()) <= b:
        flag = True
        if i == 0:
            print("Watermelon")
        elif i == 1:
            print("Pomegranates")
        else:
            print("Nuts")
        break
if flag == False:
    print("Nothing")