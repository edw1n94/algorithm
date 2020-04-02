def solution(tickets):
    answer = []

    tickets2 = {}

    for i in range(0, len(tickets)):
        if tickets2.get(tickets[i][0]) == None:
            tickets2[tickets[i][0]] = [tickets[i][1]]
        else:
            tickets2[tickets[i][0]].append(tickets[i][1])

    def dfs(tickets, index, visited, expression, answer):

        start = tickets[index][0]
        dest = tickets[index][1]

        if expression == "":
            expression += start

        expression += " " + dest
        visited.append(index)

        if len(visited) == len(tickets):
            answer.append(expression)

        for index in range(0, len(tickets)):
            if index not in visited and tickets[index][0] == dest:
                dfs(tickets, index, visited.copy(), expression, answer)

    for i in range(0, len(tickets)):
        if tickets[i][0] == "ICN":
            (dfs(tickets, i, [], "", answer))

    answer = sorted(answer)

    return str.split(answer[0])


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
tickets2 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
answer = solution(tickets)
