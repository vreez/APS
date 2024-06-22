import sys; sys.stdin = open("1408.txt", "r")

sh, sm, ss = map(int, input().split(":"))
eh, em, es = map(int, input().split(":"))

start = sh * 3600 + sm*60 + ss
end = eh * 3600 + em* 60 + es
ans = end - start
if ans < 0:
    ans += 60 * 60 * 24
nh = ans // 3600
nm = (ans % 3600) // 60
ns = ans % 60
print("{:02d}:{:02d}:{:02d}".format(nh, nm, ns))