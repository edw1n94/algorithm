def solution(number, k):
    answer = ''
    number = list(number)
    for times in range(0, k):
        max = ""
        len_number = len(number)
        max_index = 0
        for index in range(0, len_number):
            num = list.copy(number)
            num.pop(index)
            num = ''.join(num)
            if (num) > max:
                max = (num)
                max_index = index

        number.pop(max_index)

    answer = ''.join(number)
    return answer


number = "4177252841"
k = 4
answer = solution(number, k)
print(answer)
