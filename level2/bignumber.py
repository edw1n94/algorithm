def solution(number, k):
    collected = []
    a = k
    for index in range(0, len(number)):

        i = len(collected)

        while (i > 0 and a > 0):
            if collected[i - 1] < number[index]:
                collected.pop(i - 1)
                a -= 1
            i -= 1
        collected.append(number[index])

    if len(number) == len(collected):
        return ''.join((collected[:len(collected) - len(collected) - k]))

    return ''.join(collected)


number = "777777"

k = 4
answer = solution(number, k)
print(answer)
