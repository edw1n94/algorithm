from itertools import permutations


def solution(numbers):
    def is_prime_bad(n: int) -> bool:
        n = int(n)
        if n < 2:
            return False
        for i in range(2, n):
            if n % i is 0:
                return False
        return True

    answer = 0

    number_list = [i for i in numbers]
    my_list = []

    for i in range(0, len(numbers) + 1):
        new_list = (list(permutations(number_list, i)))

        for j in range(0, len(new_list)):
            sum = ""
            for a in range(0, i):
                sum = sum + new_list[j][a]
                my_list.append(int(sum))

    ex_list = list(set(my_list))
    ex_list = sorted(ex_list)

    for index in ex_list:
        if is_prime_bad(index) is True:
            answer += 1
            print(index)

    return answer


numbers = "011"

answer = solution(numbers)
print(answer)
