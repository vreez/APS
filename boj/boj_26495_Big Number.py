import sys; sys.stdin = open("26495.txt", "r")

zero = """0000 
0  0 
0  0 
0  0 
0000 """
one = """   1 
   1 
   1 
   1 
   1 """
two = """2222 
   2 
2222 
2
2222 """
three = """3333 
   3 
3333 
   3 
3333 """
four = """4  4 
4  4 
4444 
   4 
   4 """
five = """5555 
5 
5555 
   5 
5555 """
six = """6666 
6 
6666 
6  6 
6666 """
seven = """7777 
   7 
   7 
   7 
   7 """
eight = """8888 
8  8 
8888 
8  8 
8888 """
nine = """9999 
9  9 
9999 
   9 
   9 """
num = list(input())
for i in range(len(num)):
    if num[i] == "0":
        print(zero)
    elif num[i] == "1":
        print(one)
    elif num[i] =="2":
        print(two)
    elif num[i] == "3":
        print(three)
    elif num[i] == "4":
        print(four)
    elif num[i] == "5":
        print(five)
    elif num[i] == "6":
        print(six)
    elif num[i] == "7":
        print(seven)
    elif num[i] == "8":
        print(eight)
    else:
        print(nine)
    if i != len(num)-1:
        print()
