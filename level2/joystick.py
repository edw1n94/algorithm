def solution(name):
    answer = 0
    reverse_name = ""

    if name[1] == 'A':
        answer -= 1

    for i in range(0, len(name)):

        if ord((name[i])) - ord('A') < ord('Z') - ord((name[i])):
            answer += ord((name[i])) - ord('A')
        else:
            answer += ord('Z') - ord((name[i])) + 1

        if i < len(name) - 1:
            answer += 1
        else:
            break

    return answer


name = "JAN"

answer = solution(name)
print(answer)
