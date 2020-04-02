def solution(begin, target, words):
    def transformatable(words1, words2):
        words1 = list(words1)
        words2 = list(words2)
        same = 0
        for i in range(0, len(words1)):
            if words1[i] == words2[i]:
                same += 1

        if same == len(words1) - 1:
            return True

        return False

    words_dict = {}

    for index in range(0, len(words)):
        if words_dict.get(index) == None:
            words_dict[index] = []

        for j in range(0, len(words)):
            if index != j and transformatable(words[index], words[j]):
                words_dict[index].append(j)

    global answer
    answer = 0

    def bfs(start, visited):
        global answer

        visited.append(start)
        if words[start] == target:
            if answer == 0:
                answer = len(visited)

            elif answer > 0:
                if answer > len(visited):
                    answer = len(visited)
            return

        next = list(set(words_dict[start]) - set(visited))

        for i in range(0, len(next)):
            bfs(next[i], visited.copy())

    for index in range(0, len(words)):
        if transformatable(words[index], begin):
            bfs(index, [])

    return answer


begin = "hit"
target = "hot"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
words2 = ["hot", "dot", "dog", "lot", "log"]

words3 = ["hhh", "hht"]
print(solution(begin, target, words))
