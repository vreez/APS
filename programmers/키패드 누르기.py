def solution(numbers, hand):
    right = [3, 6, 9]
    left = [1, 4, 7]
    middle = [2, 5, 8, 0]

    phone = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 2]]

    cur_right = [3, 2]
    cur_left = [3, 0]
    answer = ''

    for i in range(len(numbers)):
        location = [phone[numbers[i]][0], phone[numbers[i]][1]]
        if numbers[i] in right:
            answer += 'R'
            cur_right = location
        elif numbers[i] in left:
            answer += 'L'
            cur_left = location
        else:
            l = abs(cur_left[0] - phone[numbers[i]][0]) + abs(cur_left[1] - phone[numbers[i]][1])
            r = abs(cur_right[0] - phone[numbers[i]][0]) + abs(cur_right[1] - phone[numbers[i]][1])
            if l < r:
                answer += 'L'
                cur_left = location
            elif l > r:
                answer += 'R'
                cur_right = location
            else:
                if hand == 'right':
                    answer += 'R'
                    cur_right = location
                else:
                    answer += 'L'
                    cur_left = location

    return answer