def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(len(phone_book) - 1):
        if answer == False:
            break
        for j in range(i + 1, len(phone_book)):
            if len(phone_book[i]) <= len(phone_book[j]):
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    answer = False
                    break
    return answer