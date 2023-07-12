import sys; sys.stdin = open("26863.txt", "r")

table = []
for i in range(4):
    table.append(int(input()))
plus = int(input())
check = True

new = set(table)
if len(new) == 1:
    check = True
elif len(new) == 2:
    if min(table) + plus == max(table) and table.count(min(table)) == 1:
        check = True
    else:
        check = False
else:
    check = False

if check == True:
    print(1)
else:
    print(0)
