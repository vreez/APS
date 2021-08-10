def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    # 정렬을 했기 때문에 근접해 있는 수를 앞 뒤로 하나씩 확인하면서 
    # 길이가 더 짧은 숫자가 길이가 긴 숫자의 접두어인지를 확인한다.
    for i in range(len(phone_book) - 1):
        if answer == False:
            break
        if len(phone_book[i]) < len(phone_book[i + 1]):
            if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
                answer = False
                break
    return answer