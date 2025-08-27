tp1 = ('토끼','하얀색','초식')
tp2 = ('호랑이','주황색','육식')

for i in range(3):
    if i == 0:
        print("동물이름:", end=" ")
    elif i == 1:
        print("색깔:", end=" ")
    else:
        print("식성:", end=" ")
    print(tp1[i], end=" ")
    print("vs", end=" ")
    print(tp2[i], end=" ")
    print()
