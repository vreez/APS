import sys; sys.stdin = open("10173.txt", "r")

while True:
    arr = input()
    if arr == "EOI":
        break
    else:
        arr = arr.upper()
        new_arr = arr.replace(",", "")
        word = "NEMO"
        new = list(new_arr.split())
        if word in new:
            print("Found")
        else:
            print("Missing")
