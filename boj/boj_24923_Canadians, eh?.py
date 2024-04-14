import sys; sys.stdin = open("24923.txt", "r")

text = input()
if text[-3:] == "eh?":
    print("Canadian!")
else:
    print("Imposter!")