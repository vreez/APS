import sys; sys.stdin = open("1371.txt", "r")

arr = sys.stdin.read()
new = arr.replace("\n","").replace(" ","")

dict = {
    "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0,
    "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0,
    "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0,
    "y":0, "z":0
}

for i in range(len(new)):
    dict[new[i]] += 1

max_key = [m for m,n in dict.items() if max(dict.values()) == n]
for i in range(len(max_key)):
    print(max_key[i], end="")
