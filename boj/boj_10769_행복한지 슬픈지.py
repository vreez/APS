import sys; sys.stdin = open("10769.txt", "r")

happy = ':-)'
sad = ':-('
words = input()
hCount = words.count(happy)
sCount = words.count(sad)

if hCount == 0 and sCount == 0:
    print('none')
elif hCount > 0 and hCount > sCount:
    print('happy')
elif sCount > 0 and sCount > hCount:
    print('sad')
elif hCount > 0 and hCount == sCount:
    print('unsure')
