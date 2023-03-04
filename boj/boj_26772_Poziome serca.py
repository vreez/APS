import sys; sys.stdin = open("26772.txt", "r")

N = int(input())
heart = [
" @@@   @@@ ",
"@   @ @   @",
"@    @    @",
"@         @",
" @       @ ",
"  @     @  ",
"   @   @   ",
"    @ @    ",
"     @     "
]

for i in range(len(heart)):
    for j in range(N):
        print(heart[i], end= " ")
    print()