one = list(map(int, input().split()))
two = list(map(int, input().split()))
three = list(map(int, input().split()))

print("1번째 학생의 점수 2번째 학생의 점수 3번째 학생의 점수 국어 영어 수학 총점")
print(" 1번{}{}{}  {}".format(str(one[0]).rjust(4), str(one[1]).rjust(5), str(one[2]).rjust(5), str(sum(one))).rjust(5))
print(" 2번{}{}{}  {}".format(str(two[0]).rjust(4), str(two[1]).rjust(5), str(two[2]).rjust(5), str(sum(two))).rjust(5))
print(" 3번{}{}{}  {}".format(str(three[0]).rjust(4), str(three[1]).rjust(5), str(three[2]).rjust(5), str(sum(three))).rjust(5))
print("합계{}{}{}  {}".format(str(one[0]+two[0]+three[0]).rjust(4), str(one[1]+two[1]+three[1]).rjust(5), str(one[2]+two[2]+three[2]).rjust(5), str(sum(one) + sum(two) + sum(three))).rjust(5))