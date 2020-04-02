def solution(numbers, target):
    answer = []

    numbers.insert(0, 0)

    def dfs(numbers, expression, index, num, target):

        expression += eval("+" + str(num))
        if (expression) == target and index == len(numbers) - 1:
            answer.append((expression))

        if index < len(numbers) - 1:
            dfs(numbers, expression, index + 1, numbers[index + 1], target)
            dfs(numbers, expression, index + 1, -numbers[index + 1], target)

        return

    dfs(numbers, 0, 0, numbers[0], target)

    return len(answer)


numbers = [1, 1, 1, 1, 1, ]
target = 3
answer = solution(numbers, target)
print("answer = ", answer)
