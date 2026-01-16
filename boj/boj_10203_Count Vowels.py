n = int(input())
for i in range(n):
    word = input()
    ans = word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")
    print("The number of vowels in {} is {}.".format(word, ans))
