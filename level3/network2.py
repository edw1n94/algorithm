import numpy as np


def solution(n, computers):
    com = {}
    for i in range(0, n):
        com[i] = set()
        for j in range(0, n):
            if i != j and computers[i][j] == 1:
                com[i].add(j)

    def dfs(graph, start):
        visited = []
        stack = [start]

        while stack:
            n = stack.pop()
            if n not in visited:
                visited.append(n)
                stack += graph[n] - set(visited)
        return visited

    def bfs(graph, start):
        visited = []
        queue = [start]

        while queue:
            n = queue.pop(0)
            if n not in visited:
                visited.append(n)
                queue += graph[n] - set(visited)
        return visited

    graph_list = []
    print(com)
    for index in range(0, n):
        graph = sorted(bfs(com, index))
        if graph not in graph_list:
            graph_list.append(graph)

    return len(graph_list)


n = 4
computers = [[1, 0, 0, 1], [0, 1, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1]]

answer = solution(n, computers)
print(answer)
