import time

now = time.localtime()
a = 0
print(a)
a = now.tm_year-1900
print(a)
a += now.tm_mon-1
a += now.tm_mday
print(a)


