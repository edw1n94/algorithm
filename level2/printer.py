def solution(priorities, location):
    answer = 0

    sorted_priorities = sorted(priorities, reverse=True)
    priorities = [[i, priorities[i]] for i in range(0, len(priorities))]

    while len(priorities) > 0:
        flag = True
        target = priorities.pop(0)
        if target[1] != sorted_priorities[0]:
            priorities.append(target)
        else:
            answer += 1
            sorted_priorities.pop(0)
            if target[0] == location:
                return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0

answer = solution(priorities, location)
print(answer)
