def name(n):
    if n >= 10:
        return
    print("홍길동")
    name(n+1)
name(0)