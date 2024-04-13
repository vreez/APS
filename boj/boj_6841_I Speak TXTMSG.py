import sys; sys.stdin = open("6841.txt", "r")
trans = ["see you", "I’m happy", "I’m unhappy", "wink",
         "stick out my tongue", "sleepy", "totally awesome",
         "Canadian Computing Competition", "because", "thank-you",
         "you’re welcome"]
while True:
    text = input()
    if text == "TTYL":
        print("talk to you later")
        break
    else:
        if text == "CU":
            print(trans[0])
        elif text == ":-)":
            print(trans[1])
        elif text == ":-(":
            print(trans[2])
        elif text == ";-)":
            print(trans[3])
        elif text == ":-P":
            print(trans[4])
        elif text == "(~.~)":
            print(trans[5])
        elif text == "TA":
            print(trans[6])
        elif text == "CCC":
            print(trans[7])
        elif text == "CUZ":
            print(trans[8])
        elif text == "TY":
            print(trans[9])
        elif text == "YW":
            print(trans[10])
        else:
            print(text)

