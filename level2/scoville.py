import heapq


def solution(scoville, K):
    def is_done(scoville, K):
        for i in scoville:
            if i < K:
                return False
        return True

    answer = 0

    heapq.heapify(scoville)

    while (is_done(scoville, K) == False):

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        if len(scoville) <= 2:
            if (first + second * 2) < K:
                return -1

        heapq.heappush(scoville, (first + (second * 2)))
        answer += 1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7

answer = solution(scoville, K)
print(answer)
