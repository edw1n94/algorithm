def solution(citations):
    answer = 0

    def count_h(num, citations):
        for index in range(0, len(citations)):
            if citations[index] < num:
                return index

        return len(citations)

    sorted_citations = sorted(citations, reverse=True)

    for index in range(0, sorted_citations[0]):
        h = count_h(index, sorted_citations)
        if h >= index:
            if answer <= index:
                answer = index

    return answer


citations = [3, 0, 6, 1, 5, 5, 8, 11]
# sorted_citations = [0,1,3,5,5,6,8,11]

answer = solution(citations)
print(answer)
