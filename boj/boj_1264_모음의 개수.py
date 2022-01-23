import sys; sys.stdin = open("1264.txt", "r")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

while True:
    result = 0
    words = input()
    if words == "#":
        break
    else:
        for i in range(len(words)):
            if words[i] in vowels:
                result += 1
        print(result)
