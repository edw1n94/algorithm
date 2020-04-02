def solution(progresses, speeds):
    answer = []
    current = list.copy(progresses)

    day = 0
    prime = 0
    while (len(progresses) > 0):
        complete = 0
        # 개발 단계 증가
        for i in range(0, len(progresses)):
            progresses[i] += speeds[i]

        # 배포 과정
        while (len(progresses) > 0):
            if progresses[0] > 100:
                complete += 1
                progresses.pop(0)
                speeds.pop(0)
            else:
                break
        if complete > 0:
            answer.append(complete)

        # 하루 지남
        day += 1

    return answer


progresses = [40, 93, 30, 55, 60, 65]
speeds = [60, 1, 30, 5, 10, 7]

answer = solution(progresses, speeds)
print(answer)
