import sys; sys.stdin = open("4583.txt", "r")
alpha = ["b", "d", "p", "q", "i", "o", "v", "w", "x"]
while True:
    word = list(input())
    flag = True
    if len(word) == 1 and word[0] =="#":
        break
    else:
        ans = ""
        new = word[::-1]
        for i in range(len(new)):
            if new[i] not in alpha:
                flag = False
                break
            else:
                if new[i] == "b":
                    ans += "d"
                elif new[i] == "d":
                    ans += "b"
                elif new[i] == "p":
                    ans += "q"
                elif new[i] == "q":
                    ans += "p"
                else:
                    ans += new[i]
        if flag == True:
            print(ans)
        else:
            print("INVALID")