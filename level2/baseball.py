def solution(baseball):
    answer = 0
    for i in range(len(baseball)):
        baseball[i][0] = list(str(baseball[i][0]))

    answers = [(str(i)) for i in range(123, 989)]
    aa = []
    for i in range(0, len(answers)):
        for j in range(0, len(baseball)):

            if answers[i] == '000':
                pass

            elif answers[i][0] == answers[i][1] or answers[i][0] == answers[i][2] or answers[i][1] == answers[i][
                2] or '0' in answers[i]:
                answers[i] = '000'

            else:
                strike_list = []
                strike = 0
                ball = 0

                for s in range(0, 3):
                    if answers[i][s] == baseball[j][0][s]:
                        strike += 1
                        strike_list.append(answers[i][s])

                for b in range(0, 3):
                    if (baseball[j][0][b] in answers[i]) and (baseball[j][0][b] not in strike_list):
                        ball += 1

            if baseball[j][1] == strike and baseball[j][2] == ball:
                pass
            else:
                answers[i] = '000'

    for i in range(0, len(answers)):
        if answers[i] is not '000':
            answer += 1

    return answer


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

print(solution(baseball))
