def solution(name):
    alpha = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
        'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
        'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
        'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }
    name = list(name)
    answer = 0
    cursor = 0
    front = 0
    back = 0
    # name에 있는 문자를 앞에서 부터 확인할 경우
    for i in range(len(name)):
        # A를 기준으로 해당 알파벳을 완성하기 위해 조작해야 하는 조이스틱 수
        front += min(alpha[name[i]], 26 - alpha[name[i]])
        # 커서를 이동시켜야 하는 경우의 수
        if i > 0 and name[i] != 'A':
            front += min(i - cursor, len(name) - i)
            cursor = i
    cursor = 0
    # name에 있는 문자를 뒤에서 부터 확인할 경우
    for i in range(len(name)-1, -1, -1):
        back += min(alpha[name[i]], 26 - alpha[name[i]])
        if i > 0 and name[i] != 'A':
            back += min(len(name) - i, abs(cursor - i))
            cursor = i
    answer = min(front, back)
    return answer