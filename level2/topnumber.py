def solution(numbers):
    answer = ""

    def cmp_to_key(mycmp):
        'Convert a cmp= function into a key= function'

        class K:
            def __init__(self, obj, *args):
                self.obj = obj

            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0

            def __gt__(self, other):
                return mycmp(self.obj, other.obj) > 0

            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0

            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0

            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0

            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0

        return K

    def str_sort(A, B):

        strAB = str(A) + str(B)
        strBA = str(B) + str(A)
        if strAB < strBA:
            return 0
        else:
            return -1

    numbers = sorted(numbers, key=cmp_to_key(str_sort), reverse=False)

    for number in numbers:
        answer += str(number)

    if int(answer) == 0:
        return "0"

    return answer


numbers = [0, 0, 000, 0]

print(solution(numbers))
