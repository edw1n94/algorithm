## PASS ##

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]


def solution(skill, skill_trees):
    possible_skill = []
    answer = 0
    for index in range(0, len(skill)):
        possible_skill.append(skill[0:index + 1])

    possible_skill = list((reversed(possible_skill)))

    for skill_tree in skill_trees:
        list_skill_tree = list(skill_tree)
        list_skill_tree_copy = []
        for item in list_skill_tree:
            if item in skill:
                list_skill_tree_copy.append(item)

        str = (''.join(list_skill_tree_copy))

        if len(str) == 0:
            answer += 1

        if str in possible_skill:
            answer += 1

    return answer


answer = solution(skill, skill_trees)
print(answer)
