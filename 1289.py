import sys; sys.stdin = open('1289.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    bit = input()
    cnt = 0
    # print(bit)
    for i in range(0, len(bit)-1):
        if bit[0] == '0':
            if bit[i] != bit[i+1]:
                cnt += 1
        else:
            if i == 0:
               if bit[i] != bit[i + 1]:
                   cnt += 2
               else:
                   cnt += 1
            elif bit[i] != bit[i+1]:
                cnt += 1
    print("#{} {}".format(tc, cnt))
