def solution(skills, total_sp):
    class Node:

        def __init__(self, index):
            self.sp = 0
            self.parent = 0
            self.children = []

    node_list = []

    for i in range(0, len(skills) + 2):
        node_list.append(Node(i))

    for i in range(0, len(skills)):
        parent = skills[i][0]
        child = skills[i][1]

        node_list[parent].children.append(child)
        node_list[child].parent = parent

    # total_sp를 노드만큼 나눈 개수가 최대로 가능한 sp

    for sp in range(0, int(total_sp / len(node_list) - 1) + 1):

        for i in range(0, len(node_list)):
            node_list[i].sp = 0

        queue = []
        visited = []
        for i in range(1, len(node_list)):
            if len(node_list[i].children) == 0:
                queue.append(i)
                node_list[i].sp = sp

        while (queue):

            a = queue.pop(0)
            visited.append(a)

            parent = node_list[a].parent
            node_list[parent].sp += node_list[a].sp

            # parent의 모든 node를 방문했으면 queue에 넣음
            flag = True
            for v in range(0, len(node_list[parent].children)):
                if node_list[parent].children[v] not in visited:
                    flag = False

            # 진입차수가 0이 아니면 큐에 넣지 않음
            if flag and parent != 0:
                queue.append(parent)

        # 리스트 형태로 변환
        sp_list = [node_list[i].sp for i in range(1, len(node_list))]

        if sum(sp_list) == total_sp:
            return sp_list


total_sp = 121
skills = [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]

print(solution(skills, total_sp))
