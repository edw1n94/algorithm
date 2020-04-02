def solution(n, edge):
    edge_dict = {}
    answer = 0
    for index in range(1, n + 1):
        if edge_dict.get(index) == None:
            edge_dict[index] = []

    for index in range(0, len(edge)):
        edge_dict[edge[index - 1][0]].append(edge[index - 1][1])
        edge_dict[edge[index - 1][1]].append(edge[index - 1][0])

    answer_list = [0 for i in range(0, n + 1)]

    def bfs(start, end, visited):
        visited.append(start)

        if answer_list[start] != 0 and answer_list[start] < len(visited):
            return

        if end == start:
            answer_list[start] = len(visited)

        for index in range(0, len(edge_dict[start])):
            if edge_dict[start][index] not in visited:
                bfs(edge_dict[start][index], end, visited.copy())

    for index in range(2, n + 1):
        bfs(1, index, [])

    answer = answer_list.count(max(answer_list))
    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))
