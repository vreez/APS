import sys; sys.stdin = open("22524.txt", "r")
left = "qwertasdfgzxcvb"
right = "yuiophjklnm"
while True:
    word = input()
    if word ==  "#":
        break
    else:
        ans = 0
        if word[0] in left:
            hand = "l"
        else:
            hand = "r"
        for a in word:
            if a in left and hand == "r":
                ans += 1
                hand = "l"
            elif a in right and hand == 'l':
                ans += 1
                hand = "r"
        print(ans)
