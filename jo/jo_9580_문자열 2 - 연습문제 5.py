a, b = input().split()
if a >= b:
    print("{} 가(이) 더 큽니다.".format(a))
else:
    print("{} 가(이) 더 큽니다.".format(b))

if a[:3] == b[:3]:
    print("앞의 세 문자가 같습니다.")
else:
    print("앞의 세 문자가 같지 않습니다.")