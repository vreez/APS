import sys; sys.stdin = open("26752.txt", "r")

h,m,s = map(int, input().split())
total = (h*60*60) + (m*60) + s + 1

newH = total // 60 // 60
newM = (total - (h * 60 * 60)) // 60
newS = (total - (h * 60 * 60)) % 60
if newH >= 24:
    newH = newH % 24
if newM >= 60:
    newM = newM % 60
if newS >= 60:
    newS = newS % 60
if newH < 10:
    newH = "0" + str(newH)
if newM < 10:
    newM = "0"+str(newM)
if newS < 10:
    newS = "0" + str(newS)
if newH == 0:
    newH = "00"
if newM == 0:
    newM = "00"
if newS == 0:
    newS = "00"
print("{}:{}:{}".format(newH, newM, newS))
